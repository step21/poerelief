from poerelief import db, models, epidat_parse, harvest
from loc import loc
import untangle

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

for u in urls:
  r = epidat_parse.Record()
  print "New Record created"
  d = r.pEvalRecord(r.getRecord(u))
  print u
  while d:
    s = models.Epidat(id=r.id, loc=r.loc, url=r.url, expr=r.expr, licence=r.licence, title=r.title, urld=r.urld, date=r.date, insc=r.insc, material=r.material, condition=r.condition, decoration=r.decoration, geoname=r.geoname, geotype=r.geotype, geocountry=r.geocountry, georegion=r.georegion, geocoord=r.geocoord, images=r.images, idd=r.idd, sex=r.sex, pname=r.pname, deathdate=r.deathdate, edition=r.edition, verso=r.verso, recto=r.recto, translation=r.translation, linecomm=r.linecomm, endcomm=r.endcomm, proso=r.proso, bibliography=r.bibliography)
    db.session.add(s)
    try:
      db.session.commit()
      print "New record added"
    except Exception as e:
      print "Error while adding record"
  if d != 0:
    print "Error while parsing"
