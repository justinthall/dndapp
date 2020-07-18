import json


class statblock:

    def __init__(self, name, hp, ac, stats, level):
        self.currenthp=hp
        self.data = { 'name':name,
            'level': level,
            'hp': hp,
            'ac': ac,
            'stats': {
                'strength': stats[0],
                'dexterity': stats[1],
                'constitution': stats[2],
                'intelligence': stats[3],
                'wisdom': stats[4]
            }

        }
        with open('statblocks/{}.json'.format(name), 'w') as fp:
            json.dump(self.data, fp)
    def take_damage(self,damage):
        self.currenthp=self.currenthp-damage
        return self.currenthp
    def heal_damage(self,heal):
        self.currenthp=self.currenthp+heal
        return self.currenthp
    def long_rest(self):
        self.currenthp=self.data['hp']

if __name__=='__main__':
    f = statblock('Evan', 15, 12, [12, 14, 12, 10, 8, 15, ], 1)
    a = statblock('Evant', 15, 12, [12, 14, 12, 10, 8, 15], 1)
    f.take_damage(12)
    print(f.currenthp)
    f.heal_damage(10)
    print(f.currenthp)
    f.long_rest()
    print(f.currenthp)
    d=statblock('Evxant', 15, 12, [12, 14, 12, 10, 8, 15], 1)
