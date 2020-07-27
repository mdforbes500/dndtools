#!/usr/bin/python3

import random as rd
from . import npc

class Champion(npc.NPC):
    """
    Commoner NPC template data model derived from the NPC super.
    """
    def __init__(self) -> None:
        super().__init__("Champion")
        self.cr = 9
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [20,15,14,10,14,12]
        self.modifiers = [5,2,2,0,2,1]
        self.proficiency = 4
        self.armor = 18
        self.hp = rd.randint(66,220)
        self.dicecode = "22d8 + 44"
        self.saves = {"Str": 9, "Con": 6}
        self.skills = {"Athletics": 9, "Intimidation": 5, "Perception": 6}
        self.senses = {"passive Perception": 16}
        self.languages = ["Common"]
        self.features = {
            "Indomitable": "The champion rerolls a failed saving throw.",
            "Second Wind": "As a bonus action, the champion can regain 20 hit points."
        }
        self.actions = {
            "Multiattack": "The champion makes three attacks with its greatsword or its shortbow.",
            "Greatsword": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[0]),
                "range": 5,
                "damage": self.find_damage(12, self.modifiers[0]) + self.find_damage(12, 0),
                "damage code": '2d6 + {}'.format(self.modifiers[0]),
                "damage type": "slashing"
            },
            "Shortbow": {
                "attack type": "Ranged",
                "attack mod": self.find_attk_mod(self.modifiers[1]),
                "range": 320,
                "damage": self.find_damage(6, self.modifiers[1]),
                "damage code": '1d6 + {}'.format(self.modifiers[1]),
                "damage type": "piercing"
            }
        }
        self.inventory = {}
