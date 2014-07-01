# encoding=utf-8

from poerelief import app, db, models
from flask import render_template

sitenamed = "Poetic Relief"
sitenameh = u"הקלה פיוטית"
pagetitle = "Poetic dev"
version = "0.0.1"

@app.route('/')
@app.route('/index')
def page():
	pg = ""
	return render_template("index.html", pg=pg, sitename=sitenamed, pagetitle=pagetitle, version=version)

@app.route('/doc/<int:docid>')
def epidoc(docid):
	#print docid
	s = models.Epidat.query.get(docid)
	#print s.id, s.loc, s.translation
	return str(s.id) + s.loc + s.url + s.translation + s.recto + s.verso + s.title
	
  #return render_template("index.html", pg=s.id + s.loc s.translation)

#implement doc call giving record as json

#javascript to switch texts

#implement random json array?
@app.route('/doc/random')
def random():
  pass

@app.route('/demo')
def demo():
	ret = 'var jsonLikeString = "name:red, type:blue, multiples:green, cat:brown"'
	return ret