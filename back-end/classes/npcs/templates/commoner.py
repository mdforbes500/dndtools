#!/usr/bin/python3

import random as rd
from . import npc

class Commoner(npc.NPC):
    """
    Commoner NPC template data model derived from the NPC super.
    """
    def __init__(self) -> None:
        super().__init__("Commoner")
        self.cr = 0
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [10,10,10,10,10,10]
        self.modifiers = [0,0,0,0,0,0]
        self.proficiency = 2
        self.armor = 10
        self.hp = rd.randint(1,8)
        self.dicecode = "1d8"
        self.senses = {"passive Perception": 10}
        self.languages = ["Common"]
        self.actions = {
            "Club": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[0]),
                "range": 5,
                "damage": self.find_damage(4, self.modifiers[0]),
                "damage code": '1d4 + {}'.format(self.modifiers[0]),
                "damage type": "bludgeoning"
            }
        }
        self.inventory = {}
