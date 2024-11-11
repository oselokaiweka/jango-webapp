FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /jango-webapp

COPY . .

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip --no-cache-dir && pip install -r requirements.txt --no-cache-dir

ENV DJANGO_SETTINGS_MODULE=property_webapp_project.settings

EXPOSE 8000

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

#Run server with gunicorn
CMD ["gunicorn", "--workers", "1", "property_webapp_project.wsgi:application", "--bind", "0.0.0.0:8000"]