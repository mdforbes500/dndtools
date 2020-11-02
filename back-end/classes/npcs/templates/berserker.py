#!/usr/bin/python3

import random as rd
from . import npc

class Berserker(npc.NPC):
    """
    Commoner NPC template data model derived from the NPC super.
    """
    def __init__(self) -> None:
        super().__init__("Berserker")
        self.cr = 2
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [16,12,17,9,11,9]
        self.modifiers = [3,1,3,-1,0,-1]
        self.proficiency = 2
        self.armor = 13
        self.hp = rd.randint(36,99)
        self.dicecode = "9d8 + 27"
        self.senses = {"passive Perception": 10}
        self.languages = ["Common"]
        self.features = {
            "Reckless": "At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn."
        }
        self.actions = {
            "Greataxe": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[0]),
                "range": 5,
                "damage": self.find_damage(12, self.modifiers[0]),
                "damage code": '1d12 + {}'.format(self.modifiers[0]),
                "damage type": "slashing"
            }
        }
        self.inventory = {}
