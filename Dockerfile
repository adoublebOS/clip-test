FROM python:3.8
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
COPY ./app /app
ENTRYPOINT ["uvicorn", "app.main:app"]