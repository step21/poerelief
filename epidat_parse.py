import sys
from lxml import etree
from io import StringIO, BytesIO
from loc import loc
import xmltodict
import untangle

sys.setDefaultEncoding('utf-8')

#from lxml import objectify

# Fixed baseurl for SI epidat records
baseurl = "http://steinheim-institut.de/cgi-bin/epidat?"
# The seperator
s = "-"
# specifies the format
format = "teip5"
# afaik records always start at 1
id = 1
# Fixed location for testing
#loc = "aha"#


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
    self.recto = ""
    self.rueck = ""
    self.translation = ""
    self.comm1 = ""
    self.comm2 = ""
    self.comm3 = ""
    self.bibliography = ""

#This gets a record from supplied id + loc

  def getRecord(self, loc, id):
    self.url = baseurl + "id=" + loc + s + str(id) + s + format
    #tree = etree.parse(self.url)
    #doc = etree.tostring(tree.getroot())
    ddict = untangle.parse(self.url)
    return ddict

  def pExpr(self, record, expr):
    record[]

    pass

#The following methods parse the xml for a specific value each
#This is all the values to get ... but: change to one method that populates all class attributes

  def pLicence(self, record):
    pass

  def pTitle(self, record):
    pass

  def pUrl(self, record):
    pass

  def pDate(self, record):
    return record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.history.origin.date['notBefore']

  def pInsc(self, record):
    pass

  def pMaterial(self, arg):
    return record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.physDesc.objectDesc.supportDesc.support.p

#physDEsc
#r.TEI.teiHeader.fileDesc.sourceDesc.msDesc.physDesc.objectDesc.supportDesc.support


  def pCondition(self, record):
    return record.TEI.teiHeader.fileDesc.sourceDesc.msDesc.physDesc.objectDesc.supportDesc.condition

  def pDecoration(self, record):
    pass

  def pGeoName(self, record):
    pass

  def pGeoType(self, record):
    #return type, name
    pass

  def pGeoCountry(self, record):
    pass

  def pGeoRegion(self, record):
    pass

  def pGeoCoord(self, record):
    pass

  def pGetImages(self, record):
    pass

  def pGetId(self, record):

    pass

  def pGetSex(self, record):
    pass

  def pGetPersName(self, record):
    pass

  def pGetDeathDate(self, record):
    pass

  def pGetEdition(self, record):
    pass

  def pGetRecto(self, record):
    return record.TEI.text.body.div[0].div[0].ab.cdata

  def pGetRueck(self, record):
    pass

  def pGetTranslation(self, record):
    return record.TEI.text.body.div[1].div.ab.cdata

  def pGetCommentary1(self, record):
    # r.TEI.text.body.div[3].p
    pass

  def pGetCommentary2(self, record):
    pass

  def pGetCommentary3(self, record):
    pass

  def pGetBibliography(self, record):
    pass

  def harvest(self):
    for loc in range(0, len(loc.loc)):
      print loc.loc[loc]
    pass
