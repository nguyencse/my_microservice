FROM python:3

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt update \
    && apt install gcc -y \
    && apt clean

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/