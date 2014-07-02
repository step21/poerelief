#!/usr/bin/env python
# encoding=utf-8
import sys
from poerelief import db, models, epidat_parse_bfs
#mport untangle
from xml.sax._exceptions import SAXParseException

for x in sys.argv:
  program_name = sys.argv[0]
  if len(sys.argv) > 1:
    locurl = sys.argv[1]
    if len(sys.argv) > 2:
      startid = sys.argv[2]

i = 1

q = models.Urls.query.all()
for u in q:
  r = epidat_parse_bfs.Record()
  print "Record Number", i
  print "New Record initiated"
  print "Now processing ", u.url
  #FIXME don't add if no hebrew no translation
  try:
    #don't forget - some output will be double casue evalRecord gets called twice...
    r.pEvalRecord(r.getRecord(u.url))
  except SAXParseException:
    print "SAXParse exception raised due to crappy xml"
  else:
    d = r.pEvalRecord(r.getRecord(u.url))
    if d == 0:
      print "Record parsed successfully"
      s = models.Epidat(loc=r.loc, url=r.url, licence=unicode(str(r.licence)), title=r.title, urld=r.urld, date=unicode(str(r.date)), insc=r.insc, material=r.material, condition=unicode(str(r.condition)), decoration=unicode(r.decoration), geoname=r.geoname, geotype=r.geotype, geocountry=r.geocountry, georegion=r.georegion, geocoord=r.geocoord, images=unicode(str(r.images)), idd=r.idd, sex=unicode(str(r.sex)), pname=unicode(str(r.pname)), deathdate=unicode(str(r.deathdate)), edition=unicode(r.edition), verso=unicode(r.verso), recto=unicode(r.recto), translation=unicode(r.translation), linecomm=unicode(str(r.linecomm)), endcomm=unicode(r.endcomm), proso=unicode(r.proso), bibliography=unicode(r.bibliography))
      db.session.add(s)
      try:
        db.session.commit()
        print "New record added"
        i += 1
      except SAXParseException:
        print "Error while adding record"
        if d is False:
          print "Error while parsing"
