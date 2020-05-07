FROM python:3.7.7

RUN pip install Django==3.0.5
RUN pip install uWSGI==2.0.18
WORKDIR /app
COPY hello_world /app
CMD python manage.py migrate && uwsgi --http 0.0.0.0:8080 --module hello_world.wsgi:application --check-static ./
EXPOSE 8080
