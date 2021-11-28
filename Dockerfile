FROM continuumio/miniconda3
WORKDIR /home/tester/website/
EXPOSE 433
COPY req.yml ./
RUN conda env create -f req.yml
RUN echo "source activate site" > ~/.bashrc
ENV PATH /opt/conda/envs/site/bin:$PATH
COPY . .
CMD python manage.py runserver 80.87.200.64:443