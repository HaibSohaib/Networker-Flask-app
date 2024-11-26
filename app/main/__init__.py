from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
from elasticsearch import Elasticsearch
from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Elasticsearch client setup
    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    return app
