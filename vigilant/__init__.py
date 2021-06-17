import time
import json

import docker
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
client = docker.from_env()


def get_container_name(container):
    if "vigilant.name" in container.labels:
        return container.labels["vigilant.name"]
    if container.name != None:
        return container.name
    else:
        return container.Image.split('/')[-1]


def get_status():
    data = {}
    data["running_containers"] = []
    for container in client.containers.list():
        container.reload()
        if "vigilant.enabled" in container.labels and container.labels["vigilant.enabled"] == "true":
            cont = {}
            cont["name"] = get_container_name(container)
            cont["group"] = container.labels["vigilant.group"] if "vigilant.group" in container.labels else ""
            cont["state"] = container.status
            cont["started_at"] = container.attrs["State"]["StartedAt"]
            #cont["labels"] = {key:value for (key, value) in container.labels.items() if "vigilant" in key}
            data["running_containers"].append(cont)
    return data


def get_stream():
    while True:
        yield "data: {}\n\n".format(json.dumps(get_status()))
        time.sleep(5)

from vigilant import routes, errors
