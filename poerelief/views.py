# encoding=utf-8

from poerelief import app, db, models, epidat_parse_bfs
from flask import render_template
import json
import random

sitenamed = "Poetic Relief"
sitenameh = u"תבליט פיוטי"
pagetitle = "Poetic dev"
version = "0.0.1"

@app.route('/')
@app.route('/index')
def page():
	pg = ""
	return render_template("index.html", pg=pg, sitename=sitenamed, sitenameh=sitenameh, pagetitle=pagetitle, version=version, docid='random')

@app.route('/about')
def about():
	return render_template("static.html", sitename=sitenamed, sitenameh=sitenameh, pagetitle=pagetitle, version=version)

@app.route('/faq')
def faq():
	return render_template("faq.html", sitename=sitenamed, sitenameh=sitenameh, pagetitle=pagetitle, version=version)

#This also gets a specific dataset ... not sure which is better ...
@app.route('/doc/<locid>')
def epidoc_json(locid):
	doc = models.Epidat.query.filter_by(locid=locid).first_or_404()
	data = {'availability': doc.availability, 'licence': doc.licence, 'title': doc.title, 'locid': doc.locid, 'urld': doc.urld, 'date': doc.date, 'insc': doc.insc, 'material': doc.material, 'condition': doc.condition, 'deconote': doc.deconote, 'decodesc': doc.decodesc, 'geoname': doc.geoname, 'geotype': doc.geotype, 'geocountry': doc.geocountry, 'georegion': doc.georegion, 'geocoord': doc.geocoord, 'graphics': doc.graphics, 'graphicsurl': doc.graphicsurl, 'idno': doc.idno, 'sex': doc.sex, 'pname': doc.pname, 'deathdate': doc.deathdate, 'edition': doc.edition, 'verso': doc.verso, 'recto': doc.recto, 'translation': doc.translation, 'linecomm':  doc.linecomm, 'endcomm': doc.endcomm, 'proso': doc.proso, 'bibliography': doc.bibliography}

	return json.dumps(data)

  #return render_template("index.html", pg=s.id + s.loc s.translation)

#implement doc call giving record as json

#javascript to switch texts

#this gets a random dataset
@app.route('/doc/random')
def randomdoc():
	rand = random.randrange(0, db.session.query(models.Epidat).count()) 
	doc = db.session.query(models.Epidat)[rand]
	data = {'availability': doc.availability, 'licence': doc.licence, 'title': doc.title, 'locid': doc.locid, 'urld': doc.urld, 'date': doc.date, 'insc': doc.insc, 'material': doc.material, 'condition': doc.condition, 'deconote': doc.deconote, 'decodesc': doc.decodesc, 'geoname': doc.geoname, 'geotype': doc.geotype, 'geocountry': doc.geocountry, 'georegion': doc.georegion, 'geocoord': doc.geocoord, 'graphics': doc.graphics, 'graphicsurl': doc.graphicsurl, 'idno': doc.idno, 'sex': doc.sex, 'pname': doc.pname, 'deathdate': doc.deathdate, 'edition': doc.edition, 'verso': doc.verso, 'recto': doc.recto, 'translation': doc.translation, 'linecomm':  doc.linecomm, 'endcomm': doc.endcomm, 'proso': doc.proso, 'bibliography': doc.bibliography}
	return json.dumps(data)

#this generates a specific json
@app.route('/doc/random/<locid>')
def permajson(locid):
	if locid:
		doc = models.Epidat.query.filter_by(locid=locid).first()
		data = {'availability': doc.availability, 'licence': doc.licence, 'title': doc.title, 'locid': doc.locid, 'urld': doc.urld, 'date': doc.date, 'insc': doc.insc, 'material': doc.material, 'condition': doc.condition, 'deconote': doc.deconote, 'decodesc': doc.decodesc, 'geoname': doc.geoname, 'geotype': doc.geotype, 'geocountry': doc.geocountry, 'georegion': doc.georegion, 'geocoord': doc.geocoord, 'graphics': doc.graphics, 'graphicsurl': doc.graphicsurl, 'idno': doc.idno, 'sex': doc.sex, 'pname': doc.pname, 'deathdate': doc.deathdate, 'edition': doc.edition, 'verso': doc.verso, 'recto': doc.recto, 'translation': doc.translation, 'linecomm':  doc.linecomm, 'endcomm': doc.endcomm, 'proso': doc.proso, 'bibliography': doc.bibliography}
	else:
		data = "No valid id-loc specified."
	return json.dumps(data)

#This get a specific record.
"""@app.route('/<locid>')
def permalink(locid):
	if locid:
		docid = locid
	else:
		docid = "no valid id-loc specified"
	return render_template("index.html", docid=docid, sitename=sitenamed, sitenameh=sitenameh, pagetitle=pagetitle, version=version)
"""

	"""If you write a Flask view function it’s often very handy to return a 404 error for missing entries. Because this is a very common idiom, Flask-SQLAlchemy provides a helper for this exact purpose. Instead of get() one can use get_or_404() and instead of first() first_or_404(). This will raise 404 errors instead of returning None:

	@app.route('/user/<username>')
	def show_user(username):
	    user = User.query.filter_by(username=username).first()
	    return render_template('show_user.html', user=user)

	"""
