FROM continuumio/miniconda3
ENV HOME=/app
ENV APP_HOME=/app/website
RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY req.yml ./
RUN conda env create -f req.yml
RUN echo "source activate website" > ~/.bashrc
ENV PATH /opt/conda/envs/website/bin:$PATH
#RUN echo "source activate $PROJECT" > ~/.bashrc
#ENV PATH /opt/conda/envs/$PROJECT/bin:$PATH

#COPY ./entrypoint.sh .
#RUN sed -i 's/\r$//g' /app/website/entrypoint.sh
#RUN chmod +x /app/website/entrypoint.sh

COPY . .
#ENTRYPOINT ["/app/website/entrypoint.sh"]
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:443"]
CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "testersite.wsgi"]