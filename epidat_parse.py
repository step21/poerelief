from lxml import etree
from io import StringIO, BytesIO
from loc import loc
import xmltodict
import untangle

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
loc = "aha"#


class Record(object):
  def __init__(self):
    self.id = 0
    self.loc = ""
    self.url = ""

#This get a record from supplied id + loc

  def getRecord(self, loc, id):
    self.url = baseurl + "id=" + loc + s + str(id) + s + format
    #tree = etree.parse(self.url)
    #doc = etree.tostring(tree.getroot())
    ddict = untangle.parse(self.url)
    return ddict

  def pExpr(self, expr):
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
    pass

  def pInsc(self, record):
    pass

  def pMaterial(arg):
    pass

  def pCondition(self, record):
    pass

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
    pass

  def pGetRueck(self, record):
    pass

  def pGetTranslation(self, record):
    pass

  def pGetCommentary1(self, record):
    pass

  def pGetCommentary2(self, record):
    pass

  def pGetCommentary3(self, record):
    pass

  def pGetBibliography(self, record):
    pass
