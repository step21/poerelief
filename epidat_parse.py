from lxml import etree
from io import StringIO, BytesIO
from lxml import objectify
# Fixed baseurl for SI epidat records
baseurl = "http://steinheim-institut.de/cgi-bin/epidat?"
# The seperator
s = "-"
# specifies the format
format = "teip5"
# afaik records always start at 1
id = 1
# Fixed location for testing
loc = "aha"
url = baseurl + "id=" + loc + s + str(id) + s + format

print url
tree = objectify.parse(url)
#tree = etree.parse(url)
print tree
root = tree.getroot()
print root
print(isinstance(tree.getroot(), objectify.ObjectifiedElement))
print(objectify.dump(root))
#xample
#    http://steinheim-institut.de/cgi-bin/epidat?id=hha-3361
#
#list of epidat files