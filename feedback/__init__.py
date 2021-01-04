from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix
from database import initialize_db
from feedback.models import Item

from .item import api as item_api

app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config.from_object('config')

initialize_db(app)

api = Api(
    app, version="1.0", title="Feedback API", description="Feedback API",
)
api.add_namespace(item_api)
# api.add_namespace(image_api)
