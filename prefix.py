import requests
import json
import ast

#Given token
token = "Your given token"

#Empty Array
array = ""

data = { 'token' : token , 'array' : array}
req = requests.post("http://challenge.code2040.org/api/prefix", json = data)

#Decoding json dictionary passed in
string = str(req.text)
req = ast.literal_eval(string)

print(req)
print(" ")

#Took the two different key in the json dict into different variables
prefix = req['prefix']
array = req['array']

strlen = len(prefix) #length of prefix
newArray = []

#Loop to go through array
for key in req['array']:
	#take segment of word at key from 0 - length of prefix
	if(req['prefix'] != key[:strlen]): #if prefix does not equals the segment of the word
		newArray.append(key) #Add the word to the new array

print(newArray)

#Change value from array in dictionary to the new array
data['array'] = newArray

req = requests.post("http://challenge.code2040.org/api/prefix/validate",json = data)
print(req.content)
