import requests
import json
import ast
import datetime
from datetime import timedelta

#Give token
token = "Your given token"

#Empty string
datestamp = ""

data = { 'token' : token , 'datestamp' : datestamp}
req = requests.post("http://challenge.code2040.org/api/dating", json = data)

newreq = req.json()

#Took the two different key in the json dict into different variables
interval = newreq['interval']
datestamp = newreq['datestamp']

print(datestamp)

#Made datestamp(a string data type) into datetime data type
datestamp = datetime.datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")

#Made interval into datetime data type and added it to datestamp
inter = datetime.timedelta(seconds = interval) + datestamp
inter = inter.isoformat() + 'Z' #added missing Z to the iso8601 format

print(inter)

data['datestamp'] = inter

req = requests.post("http://challenge.code2040.org/api/dating/validate",json = data)
print(req.content)
