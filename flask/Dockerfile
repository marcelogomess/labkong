FROM python:3.9.6

LABEL maintainer="Marcelo Silva <celo.gomess@gmail.com>"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app


RUN pip install -r requirements.txt

COPY . /app


CMD ["python", "./app.py"]
