#!/usr/bin/python3

from __future__ import division
import random
import math
import json

#find the hit dice range
cr_table = {
    "0":        (1,6),
    "0.125":    (7,35),
    "0.25":     (36,49),
    "0.5":      (50,70),
    "1":        (71,85),
    "2":        (86,100),
    "3":        (101,115),
    "4":        (116,130),
    "5":        (131,145),
    "6":        (146,160),
    "7":        (161,175),
    "8":        (176,190),
    "9":        (191,205),
    "10":       (206,220),
    "11":       (221,235),
    "12":       (236,250),
    "13":       (251,265),
    "14":       (266,280),
    "15":       (281,295),
    "16":       (296,310),
    "17":       (311,325),
    "18":       (326,340),
    "19":       (341,355),
    "20":       (356,400),
    "21":       (401,445),
    "22":       (446,490),
    "23":       (491,535),
    "24":       (536,580),
    "25":       (581,625),
    "26":       (626,670),
    "27":       (671,715),
    "28":       (716,760),
    "29":       (761,805),
    "30":       (806,850)
}

class NPC:
    """
    NPC: Contains a model of an NPC's basic statistics necessary for generating
    a stat block for it.
    """
    def __init__(self, name: str) -> None:
        """
        Constructor for NPC data model. Creates an empty npc model.
        """
        self.name = str(name)
        self.cr = 0
        self.size = None
        self.type = None
        self.race = None
        self.alignment = None
        self.speed = {"ground": None, "fly": None, "swim": None, "climb": None}
        self.abilities = [None,None,None,None,None,None]
        self.modifiers = [None,None,None,None,None,None]
        self.proficiency = 0
        self.armor = 0
        self.hp = 0
        self.hit_die = None
        self.dicecode = None
        self.saves = None
        self.skills = None
        self.senses = None
        self.resistance = None
        self.languages = None
        self.features = None
        self.actions = None
        self.inventory = None
        self.reactions = None

    def __del__(self):
        return None

    #Methods
    def set_name(self, name):
        self.name = name

    def update_modifiers(self):
        mods = [0,0,0,0,0,0]
        for index in range(6):
            mods[index] = (int(self.abilities[index])-10)//2
        self.modifiers = mods

    def update_perception(self):
        self.senses["passive Perception"] = 8 + self.proficiency + self.modifiers[4]

    def find_hit_dice(self):
        if self.size is "Tiny":
            self.hit_die = 4
        elif self.size is "Small":
            self.hit_die = 6
        elif self.size is "Medium":
            self.hit_die = 8
        elif self.size is "Large":
            self.hit_die = 10
        elif self.size is "Huge":
            self.hit_die = 12
        elif self.size is "Gargantuan":
            self.hit_die = 20
        else:
            raise("Not a valid size classification")

    def find_proficiency(self):
        cr_table = {
            "0":        2,
            "0.125":    2,
            "0.25":     2,
            "0.5":      2,
            "1":        2,
            "2":        2,
            "3":        2,
            "4":        2,
            "5":        3,
            "6":        3,
            "7":        3,
            "8":        3,
            "9":        4,
            "10":       4,
            "11":       4,
            "12":       4,
            "13":       5,
            "14":       5,
            "15":       5,
            "16":       5,
            "17":       6,
            "18":       6,
            "19":       6,
            "20":       6,
            "21":       7,
            "22":       7,
            "23":       7,
            "24":       7,
            "25":       8,
            "26":       8,
            "27":       8,
            "28":       8,
            "29":       9,
            "30":       9
        }
        return cr_table[str(self.cr)]

    def attack_modifier(self, modifier):
        return self.proficiency + modifier

    def find_damage(self, dicecode, mod):
        damage = sum(range(1, die+1))//die + mod*die
        return damage

    def find_cr(self):
        pass

    def spell_attack(self, modifier):
        return modifier + self.proficiency
    
    def spell_save(self, modifier):
        return 8 + modifier + self.proficiency

    def export_json(self, fh: str) -> None:
        dict = {
            "name": self.name,
            "cr": self.cr,
            "size": self.size,
            "type": self.type,
            "race": self.race,
            "alignment": self.alignment,
            "speed": self.speed,
            "abilities": [
                {"strength": self.abilities[0], "str_mod": self.modifiers[0]},
                {"dexterity": self.abilities[1], "dex_mod": self.modifiers[1]},
                {"constitution": self.abilities[2], "con_mod": self.modifiers[2]},
                {"intelligence": self.abilities[3], "int_mod": self.modifiers[3]},
                {"wisdom": self.abilities[4], "wis_mod": self.modifiers[4]},
                {"charisma": self.abilities[5], "cha_mod": self.modifiers[5]}
            ],
            "proficiency": self.proficiency,
            "armor": self.armor,
            "hp": self.hp,
            "dicecode": self.dicecode,
            "skills": self.skills,
            "senses": self.senses,
            "languages": self.languages,
            "features": self.features,
            "actions": self.actions,
            "inventory": self.inventory,
        }

        exported_json = json.dumps(dict, sort_keys=True, indent=4)
        f = open(fh, "w")
        f.write(exported_json)
        f.close()

    def import_json(self, file) -> None:
        """
        Import JSON file for NPC class.
        """
        f = open(file, "r")
        imported_json = f.read()
        dict = json.loads(imported_json)
        self.name = dict["name"]
        self.cr = dict["cr"]
        self.size = dict["size"]
        self.type = dict["type"]
        self.race = dict["race"]
        self.alignment = dict["alignment"]
        self.speed = dict["speed"]
        self.abilities = [
            dict["abilities"][0]["strength"],
            dict["abilities"][1]["dexterity"],
            dict["abilities"][2]["constitution"],
            dict["abilities"][3]["intelligence"],
            dict["abilities"][4]["wisdom"],
            dict["abilities"][5]["charisma"]
        ]
        self.modifiers = [
            dict["abilities"][0]["str_mod"],
            dict["abilities"][1]["dex_mod"],
            dict["abilities"][2]["con_mod"],
            dict["abilities"][3]["int_mod"],
            dict["abilities"][4]["wis_mod"],
            dict["abilities"][5]["cha_mod"]
        ]
        self.proficiency = dict["proficiency"]
        self.armor = dict["armor"]
        self.hp = dict["hp"]
        self.dicecode = dict["dicecode"]
        self.skills = dict["skills"]
        self.senses = dict["senses"]
        self.languages = dict["languages"]
        self.features = dict["features"]
        self.actions = dict["actions"]
        self.inventory = dict["inventory"]
        f.close()