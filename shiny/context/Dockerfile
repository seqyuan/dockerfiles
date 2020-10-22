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


RUN R -e "install.packages(c('shiny', 'rmarkdown', 'DT'), repos='https://mirrors.tuna.tsinghua.edu.cn/CRAN/')" && \
	R -e "install.packages('BiocManager', repos='https://mirrors.tuna.tsinghua.edu.cn/CRAN/')" && \
	R -e "install.packages('devtools', repos='https://mirrors.tuna.tsinghua.edu.cn/CRAN/')" && \
	R -e "install.packages(c('Seurat'), repos='http://mirrors.tuna.tsinghua.edu.cn/CRAN/')" && \
	R -e "install.packages(c('shinyFiles'), repos='http://mirrors.tuna.tsinghua.edu.cn/CRAN/')" && \	
	R -e "install.packages(c('ggsci'), repos='http://mirrors.tuna.tsinghua.edu.cn/CRAN/')" && \
	R -e "install.packages(c('magrittr'), repos='http://mirrors.tuna.tsinghua.edu.cn/CRAN/')" && \
	R -e "install.packages(c('scales'), repos='http://mirrors.tuna.tsinghua.edu.cn/CRAN/')"

RUN cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ && \
	chown shiny:shiny /var/lib/shiny-server

RUN echo "GITHUB_PAT=8ef1xxxxxxx50930dxxxx5d9e4982" >>~/.Renviron && \
	echo "export PATH=$PATH:/dockerbin" >> ~/.bashrc


ADD passwd /etc/
ADD group /etc/

EXPOSE 3838

COPY shiny-server.sh /usr/bin/shiny-server.sh
RUN chmod 755 /usr/bin/shiny-server.sh
CMD ["/usr/bin/shiny-server.sh"]

#ENV PATH $PATH

