import urllib.request
import urllib.parse
import sys
import subprocess
import os
import glob
from xml.dom import minidom
 
url = 'http://www.geoplugin.net/xml.gp?ip=167.219.48.10'
f = urllib.request.urlopen(url)
#print(f.read().decode('utf-8'))

xmldoc = minidom.parse(f)
itemlist = xmldoc.getElementsByTagName('geoplugin')