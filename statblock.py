import json


class statblock:

    def __init__(self, name, hp, ac, stats, level=0):
        self.name = name
        self.currenthp = hp
        self.temp_hp = 0
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
                     }

                     }
        with open('statblocks/{}.json'.format(name), 'w') as fp:
            json.dump(self.data, fp)

    def take_damage(self, damage):
        if self.temp_hp > 0:
            diff = self.temp_hp - damage
            if diff <= 0:
                self.temp_hp = 0
                self.currenthp = self.currenthp + diff
                return self.currenthp
            self.temp_hp = diff
            return self.currenthp
        self.currenthp = self.currenthp - damage
        if self.currenthp<=0:
            self.currenthp=0
            return "you are down!"
        return self.currenthp

    def heal_damage(self, heal):
        self.currenthp = self.currenthp + heal
        return self.currenthp

    def long_rest(self):
        self.currenthp = self.data['hp']

    def view_statblock(self):
        with open('statblocks/{}.json'.format(self.name), 'r') as fp:
            file = json.load(fp)
            return file

    def give_temp_hp(self, heal):
        self.temp_hp=self.temp_hp+heal
        return self.temp_hp
