#!/usr/bin/python3

import random as rd
from . import npc

class Bandit(npc.NPC):
    """
    Commoner NPC template data model derived from the NPC super.
    """
    def __init__(self) -> None:
        super().__init__("Bandit")
        self.cr = 0.125
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [11,12,12,10,10,10]
        self.modifiers = [0,1,1,0,0,0]
        self.proficiency = 2
        self.armor = 12
        self.hp = rd.randint(4,18)
        self.dicecode = "2d8 + 2"
        self.senses = {"passive Perception": 10}
        self.languages = ["Common"]
        self.actions = {
            "Scimitar": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[1]),
                "range": 5,
                "damage": self.find_damage(6, self.modifiers[1]),
                "damage code": '1d6 + {}'.format(self.modifiers[1]),
                "damage type": "slashing"
            },
            "Light Crossbow": {
                "attack type": "Ranged",
                "attack mod": self.find_attk_mod(self.modifiers[1]),
                "range": 5,
                "damage": self.find_damage(8, self.modifiers[1]),
                "damage code": '1d8 + {}'.format(self.modifiers[1]),
                "damage type": "piercing"
            }
        }
        self.inventory = {}
