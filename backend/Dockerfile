FROM python:3.9-alpine3.16

COPY requiments.txt /temp/requiments.txt
COPY efood /efood

WORKDIR /efood
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r /temp/requiments.txt
RUN pip install django-cors-headers
RUN adduser --disabled-password service-user

USER service-user
