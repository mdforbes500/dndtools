#!/usr/bin/python3

from __future__ import division
import random
import math
import json

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
        self.dicecode = None
        self.skills = None
        self.senses = None
        self.languages = None
        self.features = None
        self.actions = None
        self.inventory = None

    def __del__(self):
        return None

    #Methods
    def update_modifiers(self):
        mods = [0,0,0,0,0,0]
        for index in range(6):
            mods[index] = (int(self.abilities[index])-10)//2
        self.modifiers = mods

    def update_perception(self):
        self.senses["passive Perception"] = 8 + self.proficiency + self.modifiers[4]

    def find_attk_mod(self, mod):
        attk_mod = self.proficiency + mod
        return attk_mod

    def find_damage(self, die, mod):
        damage = sum(range(1, die+1))//die + mod*die
        return damage

    def find_cr(self):
        pass

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
            "cast_level": self.cast_level,
            "caster": self.caster,
            "cast_ability": self.cast_ability,
            "cast_save": self.cast_save,
            "spell_attk": self.spell_attk,
            "spell_list": self.spell_list,
            "spells": self.spells,
            "slots": self.slots
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
        self.cast_level = dict["cast_level"]
        self.caster = dict["caster"]
        self.cast_ability = dict["cast_ability"]
        self.cast_save = dict["cast_save"]
        self.spell_attk = dict["spell_attk"]
        self.spell_list = dict["spell_list"]
        self.spells = dict["spells"]
        self.slots = dict["slots"]
        f.close()