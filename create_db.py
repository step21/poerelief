# encoding=utf-8
import epidat_parse
from loc import loc
import untangle
import db_access

baseurl = "http://steinheim-institut.de/cgi-bin/epidat?id="
#baseurl for list of records
rbaseurl = "http://www.steinheim-institut.de/cgi-bin/epidat?sel="
selrecords = "&format=x&function=changelog&changesSince=20061201"
# The seperator
s = "-"
# specifies the format
format = "teip5"

class Data(db_access.DBC):
  def __init__(self):
    self.loclist = []
    self.recurls = []

  def initlocurls(self):
    for l in loc:
      self.loclist.append(rbaseurl + l + selrecords)
    return len(self.loclist)

  def initrecurls(self, loclist):
    for url in loclist:
      doc = untangle.parse(url)
      if int(doc.xml.changes['size']) > 0:
        for i in doc.xml.changes.id:
          self.recurls.append(baseurl + i.cdata + s + format)
    return len(self.recurls)

  def initdb(self)
    db = Data()
    return db

  def parseRecords(self, recurls, db):
    self.iid = 0
    conn = db.connect('sqlite')
    for r in recurls:
      rec = epidat_parse.Record()
      doc = rec.getRecord(r)
      rec.pEvalRecord(doc)
      rec.idd = iid
      iid += 1
      # ...
      dbsetDBRecord(conn, "id", rec.id)
      db.setDBRecord(conn, "loc", rec.loc)
      db.setDBRecord(conn, "url", rec.url)
      db.setDBRecord(conn, "expr", rec.expr)
      db.setDBRecord(conn, "licence", rec.licence)
      db.setDBRecord(conn, "title", rec.title)
      """  rec.urld
      rec.date
      rec.insc
      rec.material
      rec.condition
      rec.decoration
      rec.geoname
      rec.geotype
      rec.geocountry
      rec.georegion
      rec.geocoorddoc
      rec.images
      rec.idd
      rec.sex
      rec.pname
      rec.deathdate
      rec.edition
      rec.verso
      rec.recto
      rec.translation
      rec.linecomm
      rec.endcomm
      rec.proso
      rec.bibliography"""
