# encoding=utf-8

DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///teidb_dev.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEV = True
if DEV == True:
	#This means the 127.0.0.1:5000 displayed by flask might not work
	SERVER_NAME = "localhost"
else:
	SERVER_NAME = "www.poeticrelief.org"
