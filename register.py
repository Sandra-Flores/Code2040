import requests #HTTP request
import json 

#Given token
token = "Your given token"

#Github repository
github = "https://github.com/Sandra-Flores/Code2040"

#dictionary with keys token and github
data = {'token': token , 'github' : github}

#HTTP request. Takes in the register URL and a json dictionary
req = requests.post("http://challenge.code2040.org/api/register",json = data)
print (req.content)
