import requests
import json
import ast #Abstract Syntax Tree

#Given token
token = "Your given token"

#Empty string
needle = ""

#dictionary with keys token and needle
data = { 'token' : token , 'needle' : needle}

#HTTP request. Takes in the reverse URL and a json dictionary
req = requests.post("http://challenge.code2040.org/api/haystack", json = data)

#Decoding json dictionary passed in
stringreq = str(req.text)
req = ast.literal_eval(stringreq)

print(req)
print (" ")

index = 0 

#Loop to go through array
for key in req['haystack']:
	if(req['needle'] == key):
		#print(key)
		print(index) #print index if word is found in array

		break

	index = index + 1 #if word not found add one to index

data['needle'] = index

req = requests.post("http://challenge.code2040.org/api/haystack/validate",json = data)
print(req.content)
