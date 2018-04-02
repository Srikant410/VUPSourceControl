from flask import Flask
from flask import request, jsonify
#from flask.ext.cors import CORS
from suds.client import Client
import xmltodict

# Get SOAP Service via suds
url = 'http://localhost:3319/VideoGrab.svc?wsdl'
client = Client(url)
# Execute CurrentOilPrice method of SOAP
xml = client.service.GetImageById(1000)
print(xml)