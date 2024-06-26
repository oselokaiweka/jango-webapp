FROM python:3.10-slim-buster

WORKDIR /realynx_container_root

COPY requirements.txt /realynx_container_root/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /realynx_container_root/

ENV DJANGO_SETTINGS_MODULE=property_webapp_project.settings

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]