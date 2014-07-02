# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#from lxml import etree
#from io import StringIO, BytesIO
from loc import loc
from types import *
from urllib2 import urlopen
from bs4 import BeautifulSoup
#simplejson?
# Temporär JS code der abfragt  returns one json array  refreshes every so often‘’ or so
skipped = []
#Frage an Thomas - Warum <p> tags in xml?? vorgesehen in epidat?

#from lxml import objectify

# Fixed baseurl for SI epidat records
baseurl = "http://steinheim-institut.de/cgi-bin/epidat?id="
# The seperator
s = "-"
# specifies the format
format = "teip5"
# afaik records always start at 1
id = 1
# Fixed location for testing
#loc = "aha"


class Record(object):
  def __init__(self):
    self.data = {'availability': "", 'licence': "", 'title': "",'locid': "", 'urld': "", 'date': "", 'insc': "", 'material': "", 'condition': '', 'deconote': '', 'decodesc': '', 'geoname': '', 'geotype': '', 'geocountry': '', 'georegion': '', 'geocoord': '', 'graphics': '', 'graphicsurl': '', 'idno': '', 'sex': '', 'pname': '', 'deathdate': '', 'edition': '', 'verso': '', 'recto': '', 'translation': '', 'linecomm':  '', 'endcomm': '', 'proso': '', 'bibliography': ''}

#This gets a record from supplied id + loc

  def getRecord(self, url):
    o = urlopen(url)
    f = BeautifulSoup(o)
    return f

  def pEvalRecord(self, bfs):
    #availability
    a = bfs.availability
    self.data.update({'availability': a['status']})
    #licence
    self.data.update('licence', bfs.licence.re)
      #title
    self.data.update('title', bfs.title.text)
    #idno/locid
    self.data.update('locid', bfs.idno.text)
    #urld
    temp = bsf.find_all('idno')
    self.data.update('urld', temp[1].text)
    #date
    self.data.update('date', bfs.date.text) #OR bfs.date['notbefore']
    #insc
    self.data.update('insc', bfs.support.p) #OR bfs.support
    #material
    self.data.update('material', bfs.material.text)
    #condition
    self.data.update('condition', bfs.condition.text)
    #Decodescription #Decotype
    self.data.update('deconote', bfs.deconote)
    self.data.update('decodesc', bfs.decodesc)
    #Geoname
    self.data.update('geoname', bfs.geogname.find(text=True, recursive=False))
    #geotype
    self.data.update('geotype', bfs.settlement.type)
    #return type, name
    #geocountry
    self.data.update('geocountry', bfs.country.find(text=True, recursive=False)) # wie nur an text, OHNE child tag?
    #georegion
    self.data.update('georegion', bfs.region.text)
    #geocoord
    self.data.update('geocoord', bfs.geo)
    # Graphics
    self.data.update('graphics', bfs.graphic)
    self.data.update('graphicsurl', bfs.graphic['url']) #bfs.graphic.ref['foto1']
    #das gleiche für foto2, neue tabelle für fotos?
    #FIXME[1] ... check with len or so how many ... url with r.TEI.facsimile.graphic[0]['url'] + add recto verso stuff etc
  ### SEparate table for persons, graphics, to know recto vers etc ... maybe also separate for translation etc? ###
    # add stuff about authors, etc r.TEI.teiHeader.encodingDesc.classDecl.taxonomy.category ff
    self.data.update('idno', bfs.idno)
    #sex
    self.data.update('sex', bfs.person['sex'])
    #FIXME: für mehrere personen
    #person name
    self.data.update('pname', bfs.person.persname.text)
    #FIXME maybe as list with id if more than one??
    #deathdate
    self.data.update('deathdate', bfs.event['dateofdeath'])
    #edition
    self.data.update('edition', bfs.find_all("div", type="edition"))
     #recto
    self.data.update('recto', bfs.find_all("div", subtype="recto"))
    #verso
    self.data.update('verso', bfs.find_all("div", subtype="verso"))
    #translation
    self.data.update('translation', bfs.find_all("div", type="translation"))
    #linecomm
    self.data.update('linecomm', bfs.find_all("div", subtype="Zeilenkommentar"))
    #endcomm
    self.data.update('endcomm', bff.find_all("div", subtype="Endkommentar"))
    #proso
    self.data.update('proso', bfs.find_all("div", subtype="Prosopographie"))
    #bibliography
    self.data.update('bibliography', bfs.find_all("div", type="bibliography"))
    return 0

# format data as json

  def toJSON(self, record):
    #use lib for that
    ret = "title:" + self.title + "," "urld:" + self.urld +"," + "date:" + self.date + "," + "pname:" + self.pname + "," + "translation:" + self.translation
    return ret
