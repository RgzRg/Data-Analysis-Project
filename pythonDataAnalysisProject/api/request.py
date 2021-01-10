import requests
import json
import pandas as pd

url = 'http://127.0.0.1:5000/api/'
df = open("../data.csv", 'rb')
for line in df:
    dataLine = {}
    key = 1
    for elem in line:
        dataLine[key] = elem
        key += 1
    j_data = json.dumps(dataLine)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers)
