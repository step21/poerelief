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
import json
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
    try:
      self.data.update({'availability': a['status']})
    except TypeError:
      print "TypeError was raised for availability"
    #licence
    self.data.update({'licence': bfs.licence.ref})
      #title
    try:
      self.data.update({'title': bfs.title.text})
    except AttributeError:
      print "Attribute Error for title"
    
    #idno/locid
    
    try:
      self.data.update({'locid': bfs.idno.text})
    except AttributeError:
      print "Attribute Error for locid"
    #urld
    temp = bfs.find_all('idno')
    
    try:
      self.data.update({'urld': temp[1].text})
    except AttributeError:
      print "Attribute Error for urld"
    #date
    
    try:
      self.data.update({'date': bfs.date.text}) #OR bfs.date['notbefore']
    except AttributeError:
      print "Attribute Error for date"
    #insc
    self.data.update({'insc': bfs.support.p}) #OR bfs.support
    #material
    
    try:
      self.data.update({'material': bfs.material.text})
    except AttributeError:
      print "Attribute Error for material"
    #condition
    
    try:
      self.data.update({'condition': bfs.condition.text})
    except AttributeError:
      print "Attribute Error for condition"
    #Decodescription #Decotype
    self.data.update({'deconote': bfs.deconote})
    self.data.update({'decodesc': bfs.decodesc})
    #Geoname
    self.data.update({'geoname': bfs.geogname.find(text=True, recursive=False)})
    #geotype
    self.data.update({'geotype': bfs.settlement.type})
    #return type, name
    #geocountry
    self.data.update({'geocountry': bfs.country.find(text=True, recursive=False)}) # wie nur an text, OHNE child tag?
    #georegion
    try:
      self.data.update({'georegion': bfs.region.text})
    except AttributeError:
      print "AttributeError was raised for region"


    #geocoord
    self.data.update({'geocoord': bfs.geo})
    # Graphics
    self.data.update({'graphics': bfs.graphic})
    try:
      self.data.update({'graphicsurl': bfs.graphic['url']}) #bfs.graphic.ref['foto1']
    except TypeError:
      print "TypeError was raised by graphicsurl"
    #das gleiche für foto2, neue tabelle für fotos?
    #FIXME[1] ... check with len or so how many ... url with r.TEI.facsimile.graphic[0]['url'] + add recto verso stuff etc
  ### SEparate table for persons, graphics, to know recto vers etc ... maybe also separate for translation etc? ###
    # add stuff about authors, etc r.TEI.teiHeader.encodingDesc.classDecl.taxonomy.category ff
    self.data.update({'idno': bfs.idno})
    #sex
    try:
      self.data.update({'sex': bfs.person['sex']})
    except TypeError:
      print "TypeError was raised by sex"
    #FIXME: für mehrere personen
    #person name
    
    try:
      self.data.update({'pname': bfs.person.persname.text})
    except AttributeError:
      print "Attribute Error for pname"
    #FIXME maybe as list with id if more than one??
    #deathdate
    try:
      self.data.update({'deathdate': bfs.event['dateofdeath']})
    except (TypeError, KeyError):
      print "TypeError for deathdate"
    #edition
    self.data.update({'edition': bfs.find_all("div", type="edition")})
     #recto
    self.data.update({'recto': bfs.find_all("div", subtype="recto")})
    #verso
    self.data.update({'verso': bfs.find_all("div", subtype="verso")})
    #translation
    self.data.update({'translation': bfs.find_all("div", type="translation")})
    #linecomm
    self.data.update({'linecomm': bfs.find_all("div", subtype="Zeilenkommentar")})
    #endcomm
    self.data.update({'endcomm': bfs.find_all("div", subtype="Endkommentar")})
    #proso
    self.data.update({'proso': bfs.find_all("div", subtype="Prosopographie")})
    #bibliography
    self.data.update({'bibliography': bfs.find_all("div", type="bibliography")})
    return 0

# format data as json

  def toJSON(self):
  ret = json.dump(self.data)  
    return ret
