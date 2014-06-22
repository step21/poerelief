# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
from io import StringIO, BytesIO
from loc import loc
import xmltodict
import untangle
# Temporär JS code der abfragt  returns one json array  refreshes every so often‘’ or so

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
    self.id = 0
    self.loc = ""
    self.url = ""
    self.expr = ""
    self.licence = ""
    self.title = ""
    self.urld = ""
    self.date = ""
    self.insc = ""
    self.material = ""
    self.condition = ""
    self.decoration = ""
    self.geoname = ""
    self.geotype = ""
    self.geocountry = ""
    self.georegion = ""
    self.geocoord = ""
    self.images = ""
    self.idd = ""
    self.sex = ""
    self.pname = ""
    self.deathdate = ""
    self.edition = ""
    self.verso = ""
    self.recto = ""
    self.translation = ""
    self.linecomm = ""
    self.endcomm = ""
    self.proso = ""
    self.bibliography = ""

#This gets a record from supplied id + loc

  def getRecord(self, url):
    self.url = url
    rec = untangle.parse(url)
    return rec

  def pEvalRecord(self, record):
    #availability #licencename #licencelink
    self.licence = [record.TEI.teiHeader.fileDesc.publicationStmt.availability['status'], record.TEI.teiHeader.fileDesc.publicationStmt.availability.licence.ref.cdata, record.TEI.teiHeader.fileDesc.publicationStmt.availability.licence.ref['target']]
    self.title = record.TEI.teiHeader.fileDesc.titleStmt.title.cdata
    self.urld = record.TEI.teiHeader.fileDesc.publicationStmt.idno[1].cdata
    self.date = record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.history.origin.date['notBefore']
    self.insc = record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.physDesc.objectDesc.supportDesc.support.p.cdata
    self.material = record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.physDesc.objectDesc.supportDesc.support.p.material.cdata
    self.condition = record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.physDesc.objectDesc.supportDesc.condition.p.cdata
    #Decodescription #Decotype
    self.decoration = [record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.physDesc.decoDesc.decoNote.cdata, record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.physDesc.decoDesc.decoNote['type']]
    self.geoname = record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.history.origin.settlement.geogName.cdata
    self.geotype = record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.history.origin.settlement['type']
    #return type, name
    self.geocountry = record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.history.origin.country.cdata
    self.georegion = record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.history.origin.country.region.cdata
    self.geocoord = record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.history.origin.settlement.geogName.geo.cdata
    self.images = record.TEI.facsimile.graphic[0] #[1] ... check with len or so how many ... url with r.TEI.facsimile.graphic[0]['url'] + add recto verso stuff etc
    # add stuff about authors, etc r.TEI.teiHeader.encodingDesc.classDecl.taxonomy.category ff
    self.idd = record.TEI.teiHeader.fileDesc.publicationStmt.idno[0].cdata
    self.sex = record.TEI.teiHeader.profileDesc.particDesc.listPerson.person['sex'] #1 is male
    self.pname = record.TEI.teiHeader.profileDesc.particDesc.listPerson.person.persName.cdata #maybe as list with id if more than one??
    #self.deathdate = if r.TEI.teiHeader.profileDesc.particDesc.listPerson.person.event['type'] == "dateofdeath" #r.TEI.teiHeader.profileDesc.particDesc.listPerson.person.event['when']
    self.edition = record.TEI.text.body.div[0].head.cdata
    self.verso = record.TEI.text.body.div[0].div[0].ab.cdata
    self.recto = record.TEI.text.body.div[0].div[1].ab.cdata
    self.translation = record.TEI.text.body.div[1].div.ab.cdata
    self.linecomm = record.TEI.text.body.div[2].p # [0]... <head> bis Ende und dann cdata/bzw nur p als list
    self.endcomm = record.TEI.text.body.div[3].p
    self.proso = record.TEI.text.body.div[4].p
    self.bibliography = record.TEI.text.body.div[5] # if list, for p in l ... cdata
    return 0

  def harvest(self):
    ret = []
    for loc in range(0, len(loc.loc)):
      print loc.loc[loc]
      while untangle.parse(self.url):
        ret.append(baseurl + "id=" + loc + s + str(id) + s + format)
        self.id += 1
        #reset id after one loc is done
    return ret.append(baseurl + "id=" + loc + s + str(id) + s + format)

  def toJSON(self, record):
    ret = "title:" + self.title + "," "urld:" + self.urld +"," + "date:" + self.date + "," + "pname:" + self.pname + "," + "translation:" + self.translation
      # format data as json
