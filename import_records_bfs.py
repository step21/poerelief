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
      s = models.Epidat(availability=r.data['availability'], licence=unicode(str(r.data['licence'])), title=r.data['title'], locid=r.data['locid'], urld=r.data['urld'], date=unicode(str(r.data['date'])), insc=r.data['insc'], material=r.data['material'], condition=unicode(str(r.data['condition'])), deconote=unicode(r.data['deconote']), decodesc=unicode(r.data['decodesc']), geoname=r.data['geoname'], geotype=r.data['geotype'], geocountry=r.data['geocountry'], georegion=r.data['georegion'], geocoord=r.data['geocoord'], graphics=unicode(str(r.data['graphics'])), graphicsurl=r.data['graphicsurl'], idno=r.data['idno'], sex=unicode(str(r.data['sex'])), pname=unicode(str(r.data['pname'])), deathdate=unicode(str(r.data['deathdate'])), edition=unicode(r.data'[edition']), verso=unicode(r.data['verso']), recto=unicode(r.data['recto']), translation=unicode(r.data['translation']), linecomm=unicode(str(r.data['linecomm'])), endcomm=unicode(r.data['endcomm']), proso=unicode(r.data['proso']), bibliography=unicode(r.data['bibliography']))
      db.session.add(s)
      try:
        db.session.commit()
        print "New record added"
        i += 1
      except SAXParseException:
        print "Error while adding record"
        if d is False:
          print "Error while parsing"
