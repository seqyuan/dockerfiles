FROM rocker/r-ver:4.0.0 

MAINTAINER Zan Yuan <seqyuan@gmail.com>
ENV LANG=en_US.UTF-8

RUN apt-get update && apt-get install -y \
    sudo \
    gdebi-core \
    pandoc \
    pandoc-citeproc \
	libcurl4-gnutls-dev \
    libcairo2-dev \
    libxt-dev \
    xtail \
    libssl-dev \
#    libcurl4-openssl-dev \
    build-essential \
    libxml2-dev \
    libhdf5-dev \
    libudunits2-dev \
    imagemagick \
    wget

# Download and install shiny server
RUN wget --no-verbose https://download3.rstudio.org/ubuntu-14.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://download3.rstudio.org/ubuntu-14.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb && \
    . /etc/environment

RUN echo "options(BioC_mirror='https://mirrors.tuna.tsinghua.edu.cn/bioconductor')" >> ~/.Rprofile && \
		echo "options('repos' = c(CRAN='https://mirrors.tuna.tsinghua.edu.cn/CRAN/'))" >> ~/.Rprofile

RUN R -e "install.packages(c('ggplot2'', 'rmarkdown', 'DT', 'ggupset', 'devtools', ''), repos='https://mirrors.tuna.tsinghua.edu.cn/CRAN/', 'BiocManager', 'devtools')" && \
	R -e "BiocManager::install('clusterProfiler', 'enrichplot', 'DOSE', 'msigdbr', 'ReactomePA', 'org.Hs.eg.db', 'org.Mm.eg.db')"\

RUN echo "GITHUB_PAT=8ef1xxxxxxx50930dxxxx5d9e4982" >>~/.Renviron 

#ADD passwd /etc/
#ADD group /etc/

#ENV PATH $PATH

