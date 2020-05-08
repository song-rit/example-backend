FROM python:3.7.7
ENV PORT 5000
RUN pip install Django==3.0.5
RUN pip install uWSGI==2.0.18
WORKDIR /app
COPY hello_world /app
CMD python manage.py migrate && uwsgi --http 0.0.0.0:$PORT --module hello_world.wsgi:application --check-static ./
EXPOSE $PORT
