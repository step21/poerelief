#!/usr/bin/env python
from flask import Flask
from flask import render_template
#from hashlib import sha512
from epidat_demo import ...
app = Flask(__name__)

#FIXME: create page class? and then subclass and / or blueprint etc...
#how to integrate views?
sitename = "Poetic Relief"
pagetitle = "Poetic dev"
version = "0.0.1"
#fpath = "demo_chain.txt"

@app.route('/')
def page():
	pg = ""
	
	#move sha512 to class?
	#dbe = Dentry(sha512(kitten.image).hexdigest(), "phash", "This is a random kitteh", "image", "Max Muster")
	#dbe = Dentry()
	#pg = dbe.read(fpath)
	
	
	return render_template("index.html", pg=pg, sitename=sitename, pagetitle=pagetitle, version=version)

if __name__ == "__main__":
    app.run(debug = True)

# browserplugin / service to figure out what extent of content
# is what kind of license