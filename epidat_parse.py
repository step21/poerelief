from lxml import etree
# Fixed baseurl for SI epidat records
baseurl = ""
# The seperator
s = "-"
# specifies the format
format = "t"
# afaik records always start at 1
id = 1
# Fixed location for testing
loc = "aha"
url = baseurl + loc + s + id + s + format

parser = new_parser