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
    try:
      self.data.update({'licence': bfs.licence.ref})
    except TypeError:
      "TypeError was raised for licence"
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
    try:
      self.data.update({'insc': bfs.support.p}) #OR bfs.support
    except Exception:
      print "Exception for insc"
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
    try:
      self.data.update({'deconote': bfs.deconote})
    except:
      print "exception for deconote"
    try:
      self.data.update({'decodesc': bfs.decodesc})
    except Exception:
      print "exception for decodesc"
    #Geoname
    try:
      self.data.update({'geoname': bfs.geogname.find(text=True, recursive=False)})
    except Exception:
      print "Exception for Geoname"
    #geotype
    try:
      self.data.update({'geotype': bfs.settlement.type})
    except Exception:
      print "Exception for geotype"
    #geocountry
    try:
      self.data.update({'geocountry': bfs.country.find(text=True, recursive=False)}) # wie nur an text, OHNE child tag?
    except Exception:
      print "Exception for geocountry"
    #georegion
    try:
      self.data.update({'georegion': bfs.region.text})
    except AttributeError:
      print "AttributeError was raised for region"
    #geocoord
    try:
      self.data.update({'geocoord': bfs.geo})
    except Exception:
      print "Exception was raised for geocoord"
    # Graphics
    try:
      self.data.update({'graphics': bfs.graphic})
    except Exception:
      print "Exception raised for graphics"
    try:
      self.data.update({'graphicsurl': bfs.graphic['url']}) #bfs.graphic.ref['foto1']
    except TypeError:
      print "TypeError was raised by graphicsurl"
    #das gleiche für foto2, neue tabelle für fotos?
    #FIXME[1] ... check with len or so how many ... url with r.TEI.facsimile.graphic[0]['url'] + add recto verso stuff etc
  ### SEparate table for persons, graphics, to know recto vers etc ... maybe also separate for translation etc? ###
    # add stuff about authors, etc r.TEI.teiHeader.encodingDesc.classDecl.taxonomy.category ff
    try:
      self.data.update({'idno': bfs.idno})
    except Exception:
      print "Exception for idno"
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
    try:
      self.data.update({'edition': bfs.find_all("div", type="edition")})
    except Exception:
      print "Exception for edition"
    #recto
    try:
      self.data.update({'recto': bfs.find_all("div", subtype="recto")})
    except Exception:
      print "Exception for recto"
    #verso
    try:
      self.data.update({'verso': bfs.find_all("div", subtype="verso")})
    except Exception:
      print "Exception for verso"
    #translation
    try:
      self.data.update({'translation': bfs.find_all("div", type="translation")})
    except Exception:
      print "Exception for translation"
    #linecomm
    try:
      self.data.update({'linecomm': bfs.find_all("div", subtype="Zeilenkommentar")})
    except Exception:
      print "Exception for linecomm"
    #endcomm
    try:
      self.data.update({'endcomm': bfs.find_all("div", subtype="Endkommentar")})
    except Exception:
      print "Exception for endcomm"
    #proso
    try:
      self.data.update({'proso': bfs.find_all("div", subtype="Prosopographie")})
    except Exception:
      print "Exception for proso"
    #bibliography
    try:
      self.data.update({'bibliography': bfs.find_all("div", type="bibliography")})
    except Exception:
      print "Exception for bibliography"
    return 0

# format data as json

  def toJSON(self):
    ret = json.dump(self.data)  
    return ret
