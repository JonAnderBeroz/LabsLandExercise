# LabsLandExercise
## Description of the exercise

The excersise ask to get a set of data from an [api](https://labsland.com/api/labs?&country=ES&lang=es) and then convert the data to a csv file. However, not all data has to bee transformed, only thos whose educationLevels are not of a school will be transformed.

## How it was make

In order to achive the goal of getting the desired csv 3 main modules were used:
* requestsl: this module will allow us to retrieve the data from the api
* pandas: this will transform our json file to a csv file 
* json: this will allow us to encode the filtered file back into a json and to set the retrieved data of the api to a json.

With this 3 modules the implementation is straigh forward, first we will retrieve the data from the api then we will loop it and saving the data in a json format string and lastly we will parse that filtered string back to json and with panda transform it to a csv file.

Note that in order the script to work both [requests](https://pypi.org/project/requests/) and [pandas](https://pandas.pydata.org/docs/) need to be installed. Also the csv will be generated in the same folder as the python script with the name labs.csv