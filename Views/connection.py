#using no strict schema here so purely schemaless architecture will be followed here
import pymongo
import os
from pymongo import MongoClient
try:
   client = pymongo.MongoClient(f'{os.environ(["MONGO_URI"])}')
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




