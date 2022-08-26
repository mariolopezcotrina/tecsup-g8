from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate
from logging import (
    basicConfig,
    DEBUG,
    FileHandler,
    StreamHandler
)
import os

basicConfig(
    level=DEBUG,
    encoding='utf-8',
    handlers=[FileHandler('flask.log'), StreamHandler()]
)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

@app.route("/")
def index():
    return "El servidor funciona 🤠"

from app import routers