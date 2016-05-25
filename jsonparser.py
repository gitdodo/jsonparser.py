import json
from pprint import pprint

f = open('workfilejson.txt', 'w')

with open('data.json') as data_file:    
    data = json.load(data_file)

pprint(data)
strdata = json.dumps(data)
f.write(strdata)
