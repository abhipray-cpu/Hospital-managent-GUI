#using no strict schema here so purely schemaless architecture will be followed here
import pymongo
from pymongo import MongoClient
try:
   client = pymongo.MongoClient('mongodb+srv://puttanpal:puttanpal@cluster0.l891v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
   db = client["hospital"]
   admits = db["admits"]
   bills=db['bills']
   patientRecord=db['patientRecord']
   revenue=db['revenue']
   rooms=db['rooms']
   staff=db['staff']
   staffDuty=db['staffDuty']
   vehichle=db['vehichle']


except Exception as e:
   print(e)




