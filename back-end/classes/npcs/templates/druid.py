#!/usr/bin/python3

import random as rd
from . import npc

class Druid(npc.NPC):

    def __init__(self):
        super().__init__("Druid")
        self.cr = 2
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [10, 12, 13, 12, 15, 11]
        self.modifiers = [0, 1, 1, 1, 2, 0]
        self.proficiency = 2
        self.armor = 11
        self.hp = rd.randint(10, 45)
        self.dicecode = "5d8 + 5"
        self.skills = {"Medicine":4, "Nature":3, "Perception": 4}
        self.senses = {"passive Perception": 14}
        self.languages = ["Common", "Druidic", "Elven"]
        self.features = {
            "Spellcasting": {
                "caster level": 4,
                "caster ability": "Wisdom",
                "spell save": 12,
                "spell attack": 4,
                "spell list": "druid",
                "spellbook": {
                    "0": ["drudcraft", "produce flame", "shillelagh"],
                    "1": ["entangle", "longstrider", "speak with animals", "thunderwave"],
                    "2": ["animal messenger", "barkskin"],
                },
                "spell slots": {
                    "0": 0,
                    "1": 4,
                    "2": 3,
                }
            }
        }
        self.actions = {
            "Quarterstaff": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[0]),
                "range": 5,
                "damage": self.find_damage(6, self.modifiers[0]),
                "damage code": '1d6 + {}'.format(self.modifiers[0]),
                "damage type": "bludgeoning"
            }
        }
        self.inventory = {}