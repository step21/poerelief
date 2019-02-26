# encoding=utf-8

from poerelief import app, db, models, epidat_parse_bfs, logger
from flask import render_template
import json
import random
import sqlite3
import sqlalchemy

sitenamed = "Poetic Relief"
sitenameh = u"תבליט פיוטי"
pagetitle = "Poetic dev"
version = "0.0.1"

@app.route('/')
@app.route('/index')
def page():
	pg = ""
	return render_template("index.html", pg=pg, sitename=sitenamed, sitenameh=sitenameh, pagetitle=pagetitle, version=version, docid='random', servername=app.config['SERVER_NAME'])

@app.route('/about')
def about():
	return render_template("static.html", sitename=sitenamed, sitenameh=sitenameh, pagetitle=pagetitle, version=version)

@app.route('/faq')
def faq():
	return render_template("faq.html", sitename=sitenamed, sitenameh=sitenameh, pagetitle=pagetitle, version=version)


#This gives a doc as json. Why is this there in addition to the other one?
@app.route('/doc/<locid>')
def epidoc_json(locid):
	data = None
	try:
		doc = models.Epidat.query.filter_by(locid=locid).first_or_404()
		data = {'availability': doc.availability, 'licence': doc.licence, 'title': doc.title, 'locid': doc.locid, 'urld': doc.urld, 'date': doc.date, 'insc': doc.insc, 'material': doc.material, 'condition': doc.condition, 'deconote': doc.deconote, 'decodesc': doc.decodesc, 'geoname': doc.geoname, 'geotype': doc.geotype, 'geocountry': doc.geocountry, 'georegion': doc.georegion, 'geocoord': doc.geocoord, 'graphics': doc.graphics, 'graphicsurl': doc.graphicsurl, 'idno': doc.idno, 'sex': doc.sex, 'pname': doc.pname, 'deathdate': doc.deathdate, 'edition': doc.edition, 'verso': doc.verso, 'recto': doc.recto, 'translation': doc.translation, 'linecomm':  doc.linecomm, 'endcomm': doc.endcomm, 'proso': doc.proso, 'bibliography': doc.bibliography}
	except sqlalchemy.exc.OperationalError as oe:
		logger.error("Failed to connect to DB:%s", oe[0])

	return json.dumps(data)

#this gets a random dataset
@app.route('/doc/random')
def randomdoc():
	data = None
	try:
		rand = random.randrange(0, db.session.query(models.Epidat).count()) 
		doc = db.session.query(models.Epidat)[rand]
		data = {'availability': doc.availability, 'licence': doc.licence, 'title': doc.title, 'locid': doc.locid, 'urld': doc.urld, 'date': doc.date, 'insc': doc.insc, 'material': doc.material, 'condition': doc.condition, 'deconote': doc.deconote, 'decodesc': doc.decodesc, 'geoname': doc.geoname, 'geotype': doc.geotype, 'geocountry': doc.geocountry, 'georegion': doc.georegion, 'geocoord': doc.geocoord, 'graphics': doc.graphics, 'graphicsurl': doc.graphicsurl, 'idno': doc.idno, 'sex': doc.sex, 'pname': doc.pname, 'deathdate': doc.deathdate, 'edition': doc.edition, 'verso': doc.verso, 'recto': doc.recto, 'translation': doc.translation, 'linecomm':  doc.linecomm, 'endcomm': doc.endcomm, 'proso': doc.proso, 'bibliography': doc.bibliography}
	except sqlalchemy.exc.OperationalError as oe:
		logger.error("Failed to connect to DB:%s", oe[0])
		
	return json.dumps(data)

#this generates a specific json
@app.route('/doc/random/<locid>')
def permajson(locid):
	data = None
	try:
		if locid:
			doc = models.Epidat.query.filter_by(locid=locid).first()
			data = {'availability': doc.availability, 'licence': doc.licence, 'title': doc.title, 'locid': doc.locid, 'urld': doc.urld, 'date': doc.date, 'insc': doc.insc, 'material': doc.material, 'condition': doc.condition, 'deconote': doc.deconote, 'decodesc': doc.decodesc, 'geoname': doc.geoname, 'geotype': doc.geotype, 'geocountry': doc.geocountry, 'georegion': doc.georegion, 'geocoord': doc.geocoord, 'graphics': doc.graphics, 'graphicsurl': doc.graphicsurl, 'idno': doc.idno, 'sex': doc.sex, 'pname': doc.pname, 'deathdate': doc.deathdate, 'edition': doc.edition, 'verso': doc.verso, 'recto': doc.recto, 'translation': doc.translation, 'linecomm':  doc.linecomm, 'endcomm': doc.endcomm, 'proso': doc.proso, 'bibliography': doc.bibliography}
		else:
			data = "No valid id-loc specified."
	except sqlalchemy.exc.OperationalError as oe:
		logger.error("Failed to connect to DB:%s", oe[0])

	return json.dumps(data)

#This get a specific record
@app.route('/<locid>')
def permalink(locid):
	if locid:
		docid = locid
	else:
		docid = "no valid id-loc specified"
	return render_template("index.html", docid=docid, sitename=sitenamed, sitenameh=sitenameh, pagetitle=pagetitle, version=version)

