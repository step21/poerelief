# encoding=utf-8
from flask import request

DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///teidb_dev.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = True
# "outside of request context :-/"
SERVER_NAME = urlparse(request.host)
