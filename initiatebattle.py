import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
battlebase = myclient['battlebase']
battlecollection = battlebase['battles']


def start_battle(room, battle):
    battle = {
        'battle':battle,
        'room': room,
        'n': 0,
        'initiative': [],
        'round': 0}
    battlecollection.insert_one(battle)
def find_battle(room):
    query = {'room': room}
    try:
        print(query)
        battle = battlecollection.find_one(query)
    except:
        raise Exception('This room has not been found')
    return battle

def add_to_initiative(room, name, roll):
    print('got here')
    query = {'room': room}
    print('got past query')
    update = {'$push': {"initiative":(name,roll)}}
    battlecollection.update_one(query, update)
    print('works!')

def update_battle(commandRoom, battle):
    query = {'room':commandRoom}
    update = {'$set':battle}
    battlecollection.update_one(query, update)
