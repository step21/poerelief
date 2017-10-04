# encoding=utf-8
from poerelief import db, models, epidat_parse, harvest
import untangle
from xml.sax._exceptions import SAXParseException

baseurl = u"http://steinheim-institut.de/cgi-bin/epidat?id="
rbaseurl = u"http://www.steinheim-institut.de/cgi-bin/epidat?sel="
selrecords = u"&format=x&function=changelog&changesSince=20061201"
# The seperator
sep = "-"
# specifies the format
f = "teip5"

i = 1
h = harvest.Harvest()
print "Harvest Instance created"

res = models.Locs.query.all()
print "Locations loaded"

for j in res:
    print "Currently working on " + j.loc + " :)"
    url = rbaseurl + j.loc + selrecords
    print url
    doc = untangle.parse(url)
    if int(doc.xml.changes['size']) > 0:
      for k in doc.xml.changes.id:
        t = baseurl + k.cdata + sep + f
        print "Adding " + t
        s = models.Urls(loc=j.loc, url=t)
        db.session.add(s)
        db.session.commit()
        print "... added"
        i += 1

print str(i) + " urls added to db"
