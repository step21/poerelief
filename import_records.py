# encoding=utf-8
from poerelief import db, models, epidat_parse, harvest
from loc import loc
import untangle
from xml.sax._exceptions import SAXParseException


baseurl = "http://steinheim-institut.de/cgi-bin/epidat?id="
rbaseurl = "http://www.steinheim-institut.de/cgi-bin/epidat?sel="
selrecords = "&format=x&function=changelog&changesSince=20061201"
# The seperator
s = "-"
# specifies the format
format = "teip5"

h = harvest.Harvest()
print "Harvest Instance created"
temp = h.initlocurls()
print "Location urls parsed and created"
urls = h.initrecurls(temp)
print "Record URLS parsed and created"
i = 1

for u in urls:
  r = epidat_parse.Record()
  print "Record Number", i
  print "New Record created"
  print "Now processing ", u
  #FIXME don't add if no hebrew no translation
  try:
    r.pEvalRecord(r.getRecord(u))
  except SAXParseException:
    print "SAXParse exception raised due to crappy xml"
  else:
    d = r.pEvalRecord(r.getRecord(u))
    print "Record parsed successfully"
    if d == 0:
      s = models.Epidat(loc=r.loc, url=r.url, licence=unicode(str(r.licence)), title=r.title, urld=r.urld, date=unicode(str(r.date)), insc=r.insc, material=r.material, condition=unicode(str(r.condition)), decoration=unicode(r.decoration), geoname=r.geoname, geotype=r.geotype, geocountry=r.geocountry, georegion=r.georegion, geocoord=r.geocoord, images=unicode(str(r.images)), idd=r.idd, sex=unicode(str(r.sex)), pname=unicode(str(r.pname)), deathdate=unicode(str(r.deathdate)), edition=unicode(r.edition), verso=unicode(r.verso), recto=unicode(r.recto), translation=unicode(r.translation), linecomm=unicode(str(r.linecomm)), endcomm=unicode(r.endcomm), proso=unicode(r.proso), bibliography=unicode(r.bibliography))
      db.session.add(s)
      try:
        db.session.commit()
        print "New record added"
        i += 1
      except SAXParseException:
        print "Error while adding record"
        if d != 0:
          print "Error while parsing"
