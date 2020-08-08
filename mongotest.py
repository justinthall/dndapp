import pymongo
myclient= pymongo.MongoClient('mongodb://localhost:27017/')

mydb=myclient['battlebase']
mycol=mydb['battles']

myquery= {'id':5}
newvalues={'$push':{'initiative':{'$each': [('sonjackson',18),('songohan',13)]}}}

mycol.update_one(myquery,newvalues)