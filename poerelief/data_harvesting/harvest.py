# encoding=utf-8
import epidat_parse
from loc import loc
from poerelief import db, models
import untangle
#import db_access

baseurl = "http://steinheim-institut.de/cgi-bin/epidat?id="
#baseurl for list of records
rbaseurl = "http://www.steinheim-institut.de/cgi-bin/epidat?sel="
selrecords = "&format=x&function=changelog&changesSince=20061201"
# The seperator
s = "-"
# specifies the format
format = "teip5"

class Harvest(object):
  def __init__(self):
    self.loclist = []
    self.recurls = []

  def initlocurls(self):
    for l in loc:
      self.loclist.append(rbaseurl + l + selrecords)
    return self.loclist

  def initrecurls(self, loclist):
    for url in loclist:
      doc = untangle.parse(url)
      if int(doc.xml.changes['size']) > 0:
        for i in doc.xml.changes.id:
          self.recurls.append(baseurl + i.cdata + s + format)
    return self.recurls
