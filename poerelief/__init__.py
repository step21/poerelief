# encoding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object('config')
app.config.from_pyfile('config.py')

import logging
logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__)

db = SQLAlchemy(app)

from poerelief import views, models
