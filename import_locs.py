# encoding=utf-8
from poerelief import db, models, epidat_parse, harvest
from loc import loc
#import untangle
#from xml.sax._exceptions import SAXParseException

#baseurl = "http://steinheim-institut.de/cgi-bin/epidat?id="
#rbaseurl = "http://www.steinheim-institut.de/cgi-bin/epidat?sel="
#selrecords = "&format=x&function=changelog&changesSince=20061201"

i = 1
#h = harvest.Harvest()
print "Harvest Instance created"
#temp = h.initlocurls()
#print "Location urls parsed and created"

for l in loc:
  s = models.Locs(loc=l)
  db.session.add(s)
  db.session.commit()
  print "Location " + str(i) + " added"
  i += 1

print str(i) + " locations added to database"
