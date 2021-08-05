'''
    This script is for detect doublets from cellranger single cell gene expression raw matrix of one sample
    method: 
        1) scrublet: https://github.com/AllonKleinLab/scrublet
        2) DoubletDetection: https://github.com/JonathanShor/DoubletDetection 
        3) scrublet and DoubletDetection
    more details:
        1) https://mp.weixin.qq.com/s/XfrvPEzANuuHFlLv34c5nA
        2) https://mp.weixin.qq.com/s/b9NiL5NdiG5QMret5m-RXw
'''

#!/usr/bin/env python
# coding: utf-8 -*- 
import argparse
import scrublet as scr
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

import doubletdetection
import tarfile

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rc('font', size=14)
plt.rcParams['pdf.fonttype'] = 42

__author__ = 'ahworld'
__mail__ = 'seqyuan@foxmail.com'
__date__ = '20200416'
__version__ = '1.0'


def parser():
    parser=argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='author:\t{0}\nmail:\t{1}\ndate:\t{2}\nversion:\t{3}'.format(__author__, __mail__, __date__, __version__))
    parser.add_argument('-i', '--inDir', help='matrix.mtx, barcodes.tsv, genes.tsv files in the dir', dest='inDir', type=str, required=True)
    parser.add_argument('-o', '--outDir', help='output dir', dest='outDir', type=str, default=os.getcwd())
    parser.add_argument('-s', '--sample', help='output file prefix', dest='sample', type=str, default='_')
    parser.add_argument('-m', '--method', help='select method to detect doublets', dest='method', choices=['scrublet', 'doubletdetection', 'scrublet_doubletdetection'], default='scrublet_doubletdetection')

    parser.add_argument('-edr','--expected_doublet_rate', help='scrublet.Scrublet expected_doublet_rate', dest='expected_doublet_rate', type=float, default=0.06)
    parser.add_argument('-sdr','--sim_doublet_ratio', help='scrublet.Scrublet sim_doublet_ratio', dest='sim_doublet_ratio', type=float, default=2.0)

    args=parser.parse_args()
    return args


def scrublet_c(sample, inDir, outDir, expected_doublet_rate, sim_doublet_ratio, ratio_df, out_df):
    print (sample, "start scrublet")
    counts_matrix = scipy.io.mmread(os.path.join(inDir, 'matrix.mtx')).T.tocsc()
    genes = np.array(scr.load_genes(os.path.join(inDir, 'genes.tsv'), delimiter='\t', column=1))

    scrub = scr.Scrublet(counts_matrix, expected_doublet_rate=expected_doublet_rate, sim_doublet_ratio=sim_doublet_ratio)
    doublet_scores, predicted_doublets = scrub.scrub_doublets(min_counts=2, min_cells=3, min_gene_variability_pctl=85, n_prin_comps=30)

    scrub.plot_histogram()
    plt.savefig(os.path.join(outDir, "{0}_scrublet_doublet_score_histogram.pdf".format(sample)))
    print(sample, 'Running scrublet UMAP...')
    scrub.set_embedding('UMAP', scr.get_umap(scrub.manifold_obs_, 10, min_dist=0.3))
    print(sample, 'scrublet Done.')

    scrub.plot_embedding('UMAP', order_points=True)
    plt.savefig(os.path.join(outDir, "{0}_scrublet_UMAP.pdf".format(sample)))
    print (sample, "Done scrublet")

    ratio_df.loc['scrublet', sample] = scrub.detected_doublet_rate_
    out_df['scrublet_doublet_scores'] = doublet_scores
    out_df['scrublet_doublets'] = predicted_doublets

    return ratio_df, out_df

def doubletdetection_c(sample, inDir, outDir, ratio_df, out_df):
    print (sample, "start doubletdetection")

    raw_counts = doubletdetection.load_mtx(os.path.join(inDir, 'matrix.mtx'))
    # Remove columns with all 0s
    zero_genes = (np.sum(raw_counts, axis=0) == 0).A.ravel()
    raw_counts = raw_counts[:, ~zero_genes]

    clf = doubletdetection.BoostClassifier(n_iters=50, use_phenograph=False, standard_scaling=True)
    doublets = clf.fit(raw_counts).predict(p_thresh=1e-16, voter_thresh=0.5)

    f = doubletdetection.plot.convergence(clf, save=os.path.join(outDir, sample + '_doubletdetection_convergence.pdf'), show=True, p_thresh=1e-16, voter_thresh=0.5)
    f2, umap_coords = doubletdetection.plot.umap_plot(raw_counts, doublets, random_state=1, save=os.path.join(outDir, sample + '_doubletdetection_UMAP.pdf'), show=True)
    f3 = doubletdetection.plot.threshold(clf, save=os.path.join(outDir, sample + '_doubletdetection_threshold.pdf'), show=True, p_step=6)

    ratio_df.loc['doubletdetection', sample] = len(doublets[doublets > 0])/len(doublets)

    out_df['doubletdetection_doublets'] = doublets
    out_df.loc[out_df[out_df['doubletdetection_doublets']==0].index,'doubletdetection_doublets'] = False
    out_df.loc[out_df[out_df['doubletdetection_doublets']==1].index,'doubletdetection_doublets'] = True
    print (sample, "Done doubletdetection")

    return ratio_df, out_df

def main():
    args = parser()

    ratio_df = pd.DataFrame([[0],[0]],index=['scrublet', 'doubletdetection'],columns=[args.sample])
    out_df = pd.read_csv(os.path.join(args.inDir, 'barcodes.tsv'), header = None, index_col=None, names=['barcode'])

    if args.method == 'scrublet':
        ratio_df, out_df = scrublet_c(args.sample, args.inDir, args.outDir, args.expected_doublet_rate, args.sim_doublet_ratio, ratio_df, out_df)
    elif args.method == 'doubletdetection':
        ratio_df, out_df = doubletdetection_c(args.sample, args.inDir, args.outDir, ratio_df, out_df)
    else:
        ratio_df, out_df = scrublet_c(args.sample, args.inDir, args.outDir, args.expected_doublet_rate, args.sim_doublet_ratio, ratio_df, out_df)
        ratio_df, out_df = doubletdetection_c(args.sample, args.inDir, args.outDir, ratio_df, out_df)
        
    ratio_df.to_csv(os.path.join(args.outDir, args.sample + '_' + args.method + '_doublets_ratio.csv'), index=True,header=True)
    out_df.to_csv(os.path.join(args.outDir, args.sample + '_' + args.method + '_mark_doublets_barcodes.csv'), index=True,header=True)
    
if __name__ == "__main__":
    main()

