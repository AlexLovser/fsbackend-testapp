FROM python:3.9

RUN apt-get update -y && apt-get upgrade -y

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

COPY wait-for /usr/bin/
RUN chmod +x /usr/bin/wait-for
RUN chmod +x entrypoint.sh