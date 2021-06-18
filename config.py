import os
import secrets
from os.path import join, dirname
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "".join(secrets.token_hex(16))
    STATE_FILE = os.environ.get("STATE_FILE") or "./config/state.yaml"
