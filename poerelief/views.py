# encoding=utf-8

from poerelief import app

@app.route('/')
@app.route('/index')
def  index():
  return "Hello World!"

@app.route('/doc/<location>/<int:docid>')
def page(location, id):
  pass

#implement doc call giving record as json

#javascript to switch texts

#implement random json array?
@app.route('/doc/random')
def random():
  pass
