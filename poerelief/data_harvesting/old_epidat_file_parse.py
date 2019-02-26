from lxml import etree
from io import StringIO, BytesIO
from lxml import objectify

url = "hha-3361.xml"

print url

tree = objectify.parse(url)
#tree = etree.parse(url)
print "Parsed url " + str(tree)
root = tree.getroot()
#print "Root: " + str(root)
#print (isinstance(tree.getroot(), objectify.ObjectifiedElement))

#print(objectify.dump(root))
#xample
#    http://steinheim-institut.de/cgi-bin/epidat?id=hha-3361

test = objectify.Element("translation")
print test
tl = objectify.SubElement(translation, "Übersetzung")

#
#list of epidat files
