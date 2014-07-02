# encoding=utf-8

from . import db

class Epidat(db.Model):

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  availability = db.Column(db.String(12))
  licence = db.Column(db.Text)
  title = db.Column(db.Text)
  locid = db.Column(db.String(12))
  urld = db.Column(db.String(256))
  date = db.Column(db.String)
  insc = db.Column(db.Text)
  material = db.Column(db.String)
  condition = db.Column(db.String)
  deconote = db.Column(db.String)
  decodesc = db.Column(db.String)
  geoname = db.Column(db.String)
  geotype = db.Column(db.String)
  geocountry = db.Column(db.String)
  georegion = db.Column(db.String)
  geocoord = db.Column(db.String(256))
  graphics = db.Column(db.Text)
  graphicsurl = db.Column(db.String(256))
  idno = db.Column(db.String)
  sex = db.Column(db.Integer)
  pname = db.Column(db.String(120))
  deathdate = db.Column(db.String)
  edition = db.Column(db.String(120))
  recto = db.Column(db.Text)
  verso = db.Column(db.Text)
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
