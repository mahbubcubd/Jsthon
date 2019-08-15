# Parsing json from directory 
#Python 3
import json
# if the terminal open in the same directory where the json file is located
data = json.loads(open("JSON FILE NAME").read()) # e.g: data = json.loads(open("myjson.json").read())
"""Terminal Opened in any dorectory
    FOR WINDOWS: data = json.loads(open("D:\path\to\jsonfile\myjson.json").read())
    FOR Ubuntu: data = json.loads(open("/home/path/to/jsonfile/myjson.json").read())
"""
data = json.loads(open("FULL FILE PATH").read())


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
