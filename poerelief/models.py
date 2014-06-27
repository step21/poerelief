# encoding=utf-8

from . import db

class Epidat(db.Model):

  #Columns
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  loc = db.Column(db.String(12), default=0)
  url = db.Column(db.String(256))
  #expr = db.Column(db.String(256))
  licence = db.Column(db.Text)
  title = db.Column(db.Text)
  urld = db.Column(db.String)
  #FIXME convert to date object
  date = db.Column(db.String)
  insc = db.Column(db.Text)
  material = db.Column(db.String)
  condition = db.Column(db.String)
  decoration = db.Column(db.String)
  geoname = db.Column(db.String)
  geotype = db.Column(db.String)
  geocountry = db.Column(db.String)
  georegion = db.Column(db.String)
  geocoord = db.Column(db.String(256))
  images = db.Column(db.Text)
  idd = db.Column(db.String)
  sex = db.Column(db.Integer)
  pname = db.Column(db.String(120))
  #FIXME convert to date object
  deathdate = db.Column(db.String)
  edition = db.Column(db.String(120))
  verso = db.Column(db.Text)
  recto = db.Column(db.Text)
  translation = db.Column(db.Text)
  linecomm = db.Column(db.Text)
  endcomm = db.Column(db.Text)
  proso = db.Column(db.Text)
  bibliography = db.Column(db.Text)

class Locs(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  loc = db.Column(db.String(12))

class Urls(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  loc = db.Column(db.String(12))
  url = db.Column(db.String(256))
