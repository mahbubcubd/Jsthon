# Parsing json from directory 


import json
m='file directory like D:\json\js.json'
n=json.load(m)
print n;


#parsing json data from url for python 2.7
import urllib, json
url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data

#parsing json data from url for python 3
