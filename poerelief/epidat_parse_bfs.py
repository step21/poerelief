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
    self.data = {}

#This gets a record from supplied id + loc

  def getRecord(self, url):
    o = urlopen(url)
    bfs = BeautifulSoup(bfs)
    return bfs

  def pEvalRecord(self, bsf):
    #availability
    a = bsf.availability
    self.availability = a['status']
    #licence
      licence = bsf.licence.re
      #title
      self.title = bsf.title.text
    #idno/locid
    bsf.idno.text
    #urld
    temp = bsf.find_all('idno')
    urld = temp[1].text
    #date
    bfs.date.text OR bfs.date['notbefore']
    #insc
    bfs.support.p OR bfs.support
    #material
    bsf.material.text
    #condition
    bsf.condition.text
    #Decodescription #Decotype
    bfs.deconote, bfs.decodesc
    #Geoname
    eDesc.msDesc.history.origin.settlement.geogName.cdata
    #geotype
    bfs.settlement.type
    #return type, name
    #geocountry
    bfs.country # wie nur an text, OHNE child tag?
    #georegion
    bfs.region.text
    #geocoord
    bfs.geo
    # Graphics
    bfs.graphic bfs.graphic['url'] bfs.graphic.ref['foto1']
    #das gleiche für foto2, neue tabelle für fotos?
    #FIXME[1] ... check with len or so how many ... url with r.TEI.facsimile.graphic[0]['url'] + add recto verso stuff etc
  ### SEparate table for persons, graphics, to know recto vers etc ... maybe also separate for translation etc? ###
    # add stuff about authors, etc r.TEI.teiHeader.encodingDesc.classDecl.taxonomy.category ff
    bfs.idno
    #sex
   bfs.person['sex']
   #FIXME: für mehrere personen
    #person name
    bfs.person.persname.text
    #FIXME maybe as list with id if more than one??
    #deathdate
    bfs.event['dateofdeath']
    #edition
    bsf.find_all("div", type="edition")
    #verso
    bsf.find_all("div", subtype="verso")
    #recto
    bsf.find_all("div", subtype="recto")
    #translation
    bsf.find_all("div", type="translation")
    #linecomm
    bsf.find_all("div", subtype="Zeilenkommentar")
    #endcomm
    bsf.find_all("div", subtype="Endkommentar")
    #proso
    bsf.find_all("div", subtype="Prosopographie")
    #bibliography
    bsf.find_all("div", type="bibliography")
    return 0

# format data as json

  def toJSON(self, record):
    #use lib for that
    ret = "title:" + self.title + "," "urld:" + self.urld +"," + "date:" + self.date + "," + "pname:" + self.pname + "," + "translation:" + self.translation
    return ret
