
FROM python:3.10-slim

ENV APP_NAME    skill
ENV PREFIX      /opt/powertofly
ENV PREFIX_APP  ${PREFIX}/${APP_NAME}

ENV UVICORN_HOST    0.0.0.0
ENV UVICORN_PORT    5000
ENV UVICORN_APP     app.main:app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install \
  -q \
  --upgrade \
  --no-cache-dir \
    newrelic==7.2.4.171 \
    uvicorn==0.18.3

COPY ./docker-entrypoint.sh /

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install \
  --no-cache-dir \
  -q \
  -r /tmp/requirements.txt

WORKDIR ${PREFIX_APP}

COPY ./app ${PREFIX_APP}/app

USER root

RUN chmod 777 /

ENTRYPOINT [ "/docker-entrypoint.sh" ]

