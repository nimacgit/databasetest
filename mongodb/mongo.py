from pprint import pprint
from random import random

import pymongo

client = pymongo.MongoClient()
raspName = "RPI"
raspCurrentNumber = 1

def deleteAll():
    for db in client.database_names():
        client.drop_database(db)


def newrpi():
    db = client[str(raspName)]

    user = db[raspName + str(raspCurrentNumber)]

    user.insert({'name': 'nimac', 'passwrd': 'passwrd', 'id': '123', 'number': '09195258134'})
    for i in range(10):

        #user.insert({"room" + str(i): [{'name':'roomnima'+str(i)},{'module': {'name':'termo', 'address':str(i)+str(random())}},{'module':{'name':'lux', 'address':str(i)+str(random())} }]})

        user.insert({'roomname' : 'roomnima' + str(i),
                                       'module': [{'name': 'termoii', 'address': str(i) + str(random()), 'value' : '1'},
                                        {'name': 'luxii', 'address': str(i) + str(random()), 'value' : '123'},
                                        {'name': 'luxiim', 'address': str(i) + str(random()), 'value': '123'}
                                        ]})
        #                               'module1': {'name': 'luxii', 'address': str(i) + str(random()) , 'value': '12'}})
        #user.insert({'room' + str(i): {'name': 'roomnima' + str(i)},
        #                               'module': [{'name': 'termo', 'address': str(i) + str(random())},
        #                                            {'name': 'lux', 'address': str(i) + str(random())}]})



db = client['RPI']
#deleteAll()
newrpi()
raspCurrentNumber+=1
newrpi()
raspCurrentNumber+=1
newrpi()
raspCurrentNumber+=1
user = db['RPI1']

#user.create_index('module')

found = user.find_one_and_replace({"module.name":'termoii'},{"module":[{'address': '50.5236086787068928', 'name': 'termoii', 'value': '1'},
 {'address': '50.9086448960261148', 'name': 'luxinnnnni', 'value': '123'},
 {'address': '50.03065236446419972', 'name': 'luxiim', 'value': '123'}]})
found = user.find_one({"roomname":'roomnima1'})
pprint(found['module'])








print(client.database_names())
print(client[raspName].collection_names())











#client = MongoClient('localhost', 27017)

#db.createCollection("nimadb")
#posts = db.serverStatus()
#print(posts)

