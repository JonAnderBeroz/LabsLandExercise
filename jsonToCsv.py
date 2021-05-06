import requests
import json
import pandas as pd

#getting the data from the api
response = requests.get('https://labsland.com/api/labs?&country=ES&lang=es')
data = response.json()
#initialising a fresh json file
filteredFile = '{ \"laboratories\":['
#filtering and creating the wanted json
for lab in data['laboratories']:
    if not 'ms' in lab['educationLevels'] and not 'hs' in lab['educationLevels']:
        filteredFile += '{ \"name\": \"'+ lab['name'] + '\",'
        filteredFile += '\"description\": \"'+ lab['description'] + '\",'
        filteredFile += '\"institution\": \"'+ lab['institution'] + '\"},'
#removing the extra ,
filteredFile = filteredFile[:len(filteredFile)-1]
filteredFile += ']}'
#parsin the string to a json file
filteredFileParsed = json.loads(filteredFile)
#transforming the json to a csv using panda
pdObj = pd.DataFrame(filteredFileParsed['laboratories'])
pdObj.to_csv('labs.csv', index=False)
print('transformation ended')
