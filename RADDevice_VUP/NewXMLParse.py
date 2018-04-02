import xml.etree.ElementTree as ET
tree = ET.parse('items.xml')
root = tree.getroot()
#for child in root:
#    print(child.tag, child.attrib)
#for children in child:
#    print(children.tag, root[0][1].text)

for country in root.findall('./Playlist/Media'):
    rank = country.get('ID')
    name = country.get('Description')
    print(name, rank)