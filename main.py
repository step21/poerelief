#!/usr/bin/env python
from flask import Flask
from flask import render_template

#from epidat_demo import ...
app = Flask(__name__)

#FIXME: create page class? and then subclass and / or blueprint etc...
#how to integrate views?
sitename = "Poetic Relief"
pagetitle = "Poetic dev"
version = "0.0.1"


@app.route('/')
def page():
	pg = ""
	return render_template("index.html", pg=pg, sitename=sitename, pagetitle=pagetitle, version=version)

@app.route('/demo')
def demo():
	ret = 'var jsonLikeString = "name:red, type:blue, multiples:green, cat:brown"'
	return ret

if __name__ == "__main__":
    app.run(debug = True)
