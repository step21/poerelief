# encoding=utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from poerelief import views, models
