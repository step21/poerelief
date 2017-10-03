# encoding=utf-8
from flask import request

DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///teidb_dev.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEV = True
if DEV == True:
	SERVER_NAME = "localhost:5000"
else:
	SERVER_NAME = "www.poeticrelief.org"
