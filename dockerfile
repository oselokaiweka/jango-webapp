FROM python:3.10-slim-buster

WORKDIR /app

COPY requirments.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

ENV DJANGO_SETTINGS_MODULE=property_webapp_project.settings

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]