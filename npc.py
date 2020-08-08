import statblock
import json


class npc(statblock.statblock):
    def __init__(self, name, hp, ac, stats, level,job=None,race=None):
        super().__init__(name, hp, ac, stats, level)
        self.job=job
        self.currenthp='none'
        self.data = {'name': name,
                     'level': level,
                     'hp': hp,
                     'ac': ac,
                     'stats': {
                         'strength': stats[0],
                         'dexterity': stats[1],
                         'constitution': stats[2],
                         'intelligence': stats[3],
                         'wisdom': stats[4]
                     },
                    'class':job,
                     'race':race
                     }
        with open('statblocks/{}.json'.format(name), 'w') as fp:
            json.dump(self.data, fp)


f= npc('hiya',25,17,[10,10,10,10,10,10],3)
print(f.take_damage(25))