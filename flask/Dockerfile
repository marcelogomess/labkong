FROM python:3.9.6

LABEL maintainer="Marcelo Silva <celo.gomess@gmail.com>"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "./app.py"]
