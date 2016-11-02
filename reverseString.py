import requests #HTTP request
import json

#Given token
token = "Your given token"

#Empty string
string = ""

#dictionary with keys token and string
data = {'token': token , 'string' : string}

#HTTP request. Takes in the reverse URL and a json dictionary
req = requests.post("http://challenge.code2040.org/api/reverse",json = data)

string = str(req.text) #takes content from request

end = len(string)//2 
string = list(string) #make string into array to manipulate better

#for loop runs from 0 to half the length of the word passed in
#in loop we swap the letters at the beginning with the ones at the end
for x in range(0, end):
	temp = string[x] 

	string[x] = string[len(string) - 1 - x]
	string[len(string) - 1 - x] = temp

string = "".join(string) #Bring array together into a string

print(string)
print(req.content)

data['string'] = string # Change string in dictionary

#HTTP request. Takes in the validate URL and a json dictionary
req = requests.post("http://challenge.code2040.org/api/reverse/validate",json = data)
print(req.content)
