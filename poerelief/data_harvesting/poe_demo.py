# encoding=utf-8
import epidat_parse
from loc import loc
import untangle
#demo files
#df = ["aha-0046.xml", "hha-3361.xml", "rth-0002.xml"]

baseurl = "http://steinheim-institut.de/cgi-bin/epidat?"
# The seperator
s = "-"
# specifies the format
format = "teip5"
# afaik records always start at 1
id = 1

for l in loc:
  reclist = "http://www.steinheim-institut.de/cgi-bin/epidat?sel=" + l + "&format=x&function=changelog&changesSince=20061201"
  sets = untangle.parse(reclist)
  print sets
