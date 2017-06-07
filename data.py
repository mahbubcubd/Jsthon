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

#recieving and storing data to database from json
import json
def lorason():
    response.headers['content-type']='text/json'
    lrjson=request.body.read()
    loradb=json.loads(lrjson)
    name=loradb['Name']
    message=loradb['Message']
    db.lora.insert(Name=name,Message=message)
    db.commit()
    return "Json sending successful.Thank you for your submission"
