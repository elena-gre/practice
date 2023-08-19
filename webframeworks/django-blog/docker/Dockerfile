FROM python:3.11-slim


RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY ../requirements.txt /code/
COPY ../requirements_dev.txt /code/

RUN pip install -r requirements.txt
RUN pip install -r requirements_dev.txt
COPY .. /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]