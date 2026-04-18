FROM python:3.13

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFERED 1

RUN pip install --upgrade pip

COPY ./req.txt .
RUN pip install -r req.txt

COPY . .


