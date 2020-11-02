#!/usr/bin/python3

import random as rd
from . import npc

class Cultist(npc.NPC):

    def __init__(self):
        super().__init__("Cultist")
        self.cr = 0.125
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [11, 12, 10, 10, 11, 10]
        self.modifiers = [0, 1, 0, 0, 0, 0]
        self.proficiency = 2
        self.armor = 12
        self.hp = rd.randint(2, 16)
        self.dicecode = "2d8"
        self.skills = {"Deception": 2, "Religion": 2}
        self.senses = {"passive Perception": 10}
        self.languages = ["Common"]
        self.features = {
            "Dark Devotion": "The fanatic has advantage on saving throws against being charmed or frightened."
        }
        self.actions = {
            "Scimitar": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[0]),
                "range": 5,
                "damage": self.find_damage(6, self.modifiers[0]),
                "damage code": '1d6 + {}'.format(self.modifiers[0]),
                "damage type": "slashing"
            }
        }
        self.inventory = {}