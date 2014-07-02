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
      s = models.Epidat(availability=unicode(r.data['availability']), licence=unicode(r.data['licence']), title=unicode(r.data['title']), locid=unicode(r.data['locid']), urld=unicode(r.data['urld']), date=unicode(r.data['date']), insc=unicode(r.data['insc']), material=unicode(r.data['material']), condition=unicode(r.data['condition']), deconote=unicode(r.data['deconote']), decodesc=unicode(r.data['decodesc']), geoname=unicode(r.data['geoname']), geotype=unicode(r.data['geotype']), geocountry=unicode(r.data['geocountry']), georegion=unicode(r.data['georegion']), geocoord=unicode(r.data['geocoord']), graphics=unicode(r.data['graphics']), graphicsurl=unicode(r.data['graphicsurl']), idno=unicode(r.data['idno']), sex=unicode(str(r.data['sex'])), pname=unicode(r.data['pname']), deathdate=unicode(r.data['deathdate']), edition=unicode(r.data['edition']), verso=unicode(r.data['verso']), recto=unicode(r.data['recto']), translation=unicode(r.data['translation']), linecomm=unicode(r.data['linecomm']), endcomm=unicode(r.data['endcomm']), proso=unicode(r.data['proso']), bibliography=unicode(r.data['bibliography']))
      db.session.add(s)
      try:
        db.session.commit()
        print "New record added"
        i += 1
      except SAXParseException:
        print "Error while adding record"
        if d is False:
          print "Error while parsing"
