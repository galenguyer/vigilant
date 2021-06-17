FROM python:3.9-slim-buster
LABEL maintainer="Galen Guyer <galen@galenguyer.com>"

RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
    echo 'America/New_York' > /etc/timezone

RUN pip install pipenv

WORKDIR /opt/demo/

ADD Pipfile Pipfile.lock /opt/demo/

RUN pipenv install

ADD . /opt/demo/

ENTRYPOINT [ "pipenv", "run", "gunicorn", "demo:app" ]
CMD [ "--bind=0.0.0.0:8080", "--access-logfile=-" ]
