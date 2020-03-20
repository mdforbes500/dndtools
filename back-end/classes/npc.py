#!/usr/bin/python

from __future__ import division
import random
import math
import json

class NPC:
    """
    NPC: Contains a model of an NPC's basic statistics necessary for generating
    a stat block for it.
    """
    def __init__(self, name):
        """
        Constructor for NPC. Populates the character as a Commoner.
        """
        self.name = str(name)
        self.cr = 0
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(human)"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 0}
        self.abilities = [10,10,10,10,10,10]
        self.modifiers = [0,0,0,0,0,0]
        self.proficiency = 2
        self.armor = 10
        self.hp = 4
        self.dicecode = "1d8"
        self.skills = {}
        self.senses = {"passive Perception": 10}
        self.languages = ["Common"]
        self.features = {}
        self.actions = {
            "Club": [
                'Melee',
                self.find_attk_mod(self.modifiers[0]),
                5,
                self.find_damage(4, self.modifiers[0]),
                '1d4 + {}'.format(self.modifiers[0]),
                'bludgeoning'
            ],
        }
        self.inventory = {}
        self.cast_level = 0
        self.caster = False
        self.cast_ability = ""
        self.cast_save = 0
        self.spell_attk = 0
        self.spell_list = ""
        self.spells = []
        self.slots = []

    def __del__(self):
        return None;

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

    def export_json(self):
        dict = {
            "name": self.name,
            "cr": self.cr,
            "size": self.size,
            "type": self.type,
            "race": self.race,
            "alignment": self.alignment,
            "speed": self.speed,
            "abilities": [
                {"strength": self.abilities[0], "modifier": self.modifiers[0]},
                {"dexterity": self.abilities[1], "modifier": self.modifiers[1]},
                {"constitution": self.abilities[2], "modifier": self.modifiers[2]},
                {"intelligence": self.abilities[3], "modifier": self.modifiers[3]},
                {"wisdom": self.abilities[4], "modifier": self.modifiers[4]},
                {"charisma": self.abilities[5], "modifier": self.modifiers[5]}
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

        exported_json = json.dumps(dict)
        return exported_json
