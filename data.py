# Parsing json from directory 
#Python 3.6
import json
m='file directory like D:\json\js.json'
n=json.load(m)

#Parsing from URL in Python 3.6
import requests,json
data=json.loads((requests.get('YOUR URL')).content)

#parsing json data from url for python 2.7
import urllib, json
data = json.loads(urllib.urlopen('YOUR URL').read())


#Simple example of parsing json in web2py function
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
