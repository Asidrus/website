FROM continuumio/miniconda3
WORKDIR /home/tester/website/
COPY req.yml ./
RUN conda env create -f req.yml
RUN echo "source activate site" > ~/.bashrc
ENV PATH /opt/conda/envs/site/bin:$PATH
COPY . .