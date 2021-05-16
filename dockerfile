FROM python:3.8.2
ENV PYTHONUNBUFFERED 1
WORKDIR /nexiotask
COPY . /nexiotask/
RUN pip install -r requirements/dev.txt
EXPOSE 5000
CMD python manage.py runserver
