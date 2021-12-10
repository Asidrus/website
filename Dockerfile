FROM continuumio/miniconda3
ENV path=/app
ARG PROJECT='project'
ARG STORAGE='/storage/'
#RUN mkdir -m 777 $path/$PROJECT
#RUN mkdir -m 777 $path/$PROJECT/static
#RUN mkdir -m 777 $STORAGE
WORKDIR $path/$PROJECT
COPY req.yml ./
RUN conda env create -f req.yml
RUN echo "source activate $PROJECT" > ~/.bashrc
ENV PATH /opt/conda/envs/$PROJECT/bin:$PATH
COPY . .
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:443"]
CMD [ "gunicorn", "--bind", "0.0.0.0:443", "testersite.wsgi"]