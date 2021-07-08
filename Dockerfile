FROM python:3.9-slim-buster
LABEL maintainer="Galen Guyer <galen@galenguyer.com>"

RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
    echo 'America/New_York' > /etc/timezone

WORKDIR /opt/vigilant/

ADD requirements.txt /opt/vigilant/

RUN pip install -r requirements.txt

ADD . /opt/vigilant/

ENTRYPOINT [ "gunicorn", "vigilant:app" ]
CMD [ "--bind=0.0.0.0:8080", "--access-logfile=-", "--worker-class=gevent" ]
