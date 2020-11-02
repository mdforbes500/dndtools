#!/usr/bin/python3

import random as rd
from . import npc

class BanditCaptain(npc.NPC):
    """
    Commoner NPC template data model derived from the NPC super.
    """
    def __init__(self) -> None:
        super().__init__("Bandit Captain")
        self.cr = 2
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [15,16,14,14,11,14]
        self.modifiers = [2,3,2,2,0,2]
        self.proficiency = 2
        self.armor = 15
        self.hp = rd.randint(30,100)
        self.dicecode = "10d8 + 20"
        self.saves = {"Str": 4, "Dex": 5, "Wis": 2}
        self.skills = {"Athletics": 4, "Deception": 4}
        self.senses = {"passive Perception": 10}
        self.languages = ["Common", "Orcish"]
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
