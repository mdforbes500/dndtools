#!/usr/bin/python3

import random as rd
from . import npc

class Archer(npc.NPC):
    """
    Commoner NPC template data model derived from the NPC super.
    """
    def __init__(self) -> None:
        super().__init__("Archer")
        self.cr = 3
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [11,18,16,11,13,10]
        self.modifiers = [0,4,3,0,1,0]
        self.proficiency = 2
        self.armor = 16
        self.hp = rd.randint(40,110)
        self.dicecode = "10d8 + 30"
        self.skills = {"Acrobatics": 6, "Perception": 5}
        self.senses = {"passive Perception": 15}
        self.languages = ["Common"]
        self.features = {
            "Archer's Eye": {
                "usage": 3,
                "text": "As a bonus action, the archer can add 1d10 to its next attack or damage roll with a longbow or shortbow."
            }
        }
        self.actions = {
            "Multiattack" : "The archer makes two attacks with its longbow.",
            "Shortsword": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[1]),
                "range": 5,
                "damage": self.find_damage(6, self.modifiers[0]),
                "damage code": '1d6 + {}'.format(self.modifiers[0]),
                "damage type": "piercing"
            },
            "Longbow": {
                "attack type": "Ranged",
                "attack mod": self.find_attk_mod(self.modifiers[1]),
                "range": "150/600",
                "damage": self.find_damage(8, self.modifiers[0]),
                "damage code": '1d6 + {}'.format(self.modifiers[0]),
                "damage type": "piercing"
            }
        }
        self.inventory = {}
