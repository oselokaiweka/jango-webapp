FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /realynx_container_root

COPY . .

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=property_webapp_project.settings

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]