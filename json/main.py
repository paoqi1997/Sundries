#!/usr/bin/python3

'''JSON Object & Array'''

import json
import os
import sys

oDict = {
    'solution': 'db',
    'type': {
        'relational': [{
            'name': 'mysql', 'version': '8.0.19'
        }, {
            'name': 'mariadb', 'version': '10.3.22'
        }],
        'kv': [{
            'name': 'redis', 'version': '5.0.7'
        }]
    }
}

sFileName = os.path.join(
    sys.path[0], 'data.json'
)

# json.dumps: Dict -> JSON String
sJsonData = json.dumps(oDict)
print(sJsonData)

# json.loads: JSON String -> Dict
oResDict = json.loads(sJsonData)
print(oResDict)

# json.dump: Dict -> JSON File
with open(sFileName, 'w') as oFile:
    json.dump(oDict, oFile)

# json.load: JSON File -> Dict
with open(sFileName, 'r') as oFile:
    oResDict = json.load(oFile)
    print(oResDict)
