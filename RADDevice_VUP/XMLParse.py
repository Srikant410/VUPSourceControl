import sys
import subprocess
import os
import glob
from xml.dom import minidom

#path ='/home/pi/Desktop/'
path = "C:\\Users\\srprasad\\Documents\\Visual Studio 2015\\Projects\\RADDevice_VUP\\RADDevice_VUP\\"
xmldoc = minidom.parse('items.xml')
itemlist = xmldoc.getElementsByTagName('media')
print(len(itemlist))
#print(itemlist[0].attributes['name'].value)
#for s in itemlist:
#    print(s.attributes['name'].value)

for infile in glob.glob(os.path.join(path, '*.mp4')):
    for s in itemlist:        
        str = path + s.attributes['name'].value
        if infile == str:
          print(infile)
          #a = subprocess.call( [ "omxplayer", "-o", "hdmi", infile])
          break