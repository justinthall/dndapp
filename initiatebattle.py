import pymongo

myclient= pymongo.MongoClient('mongodb://localhost:27017/')
battlebase=myclient['battlebase']
battlecollection=battlebase['battles']

class battle:
    battlenumber=0

    def __init__(self):
        battle.battlenumber += 1
        self.battleid = battle.battlenumber
        self.n = 1
        self.initiative=[]
        self.round=0
        self.write_to_db()

    def add_initiatee(self,initscore,character):
        self.initiative.append((initscore,character))
        self.initiative.sort(reverse=True)
        self.update_db()

    def add_multiple(self,initscore,characters):
        for i in characters:
            self.initiative.append((initscore,i))
        self.initiative.sort(reverse=True)

    def next_turn(self):
        if self.currentturn == self.initiative[len(self.initiative)-1]:
            self.currentturn=self.initiative[0]
            self.n=1
        else:
            self.currentturn=self.initiative[self.n]
            self.n += 1

    def reshuffle(self):
        self.currentturn=self.initiative[0]
        self.n=1


    def endbattle(self):
        self.state=False
        return 'The battle has ended!'

    def write_to_db(self):
        intodb = {'id':self.battleid,'initiative': self.initiative, 'n': self.n, 'round': self.round}
        battlecollection.insert_one(intodb)

    def update_db(self):
        intodb = {'id':self.battleid,'initiative': self.initiative, 'n': self.n, 'round': self.round}
        battlecollection.update_one({'id':self.battleid},{'$set':{'initiative':self.initiative}})

b=battle()
b.add_initiatee(25,'jason')
b.add_initiatee(28,'Jason')
print(b.battleid)






