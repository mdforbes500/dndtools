#!/usr/bin/python3

import random as rd
from . import npc

class Diviner(npc.NPC):

    def __init__(self):
        super().__init__("Diviner")
        self.cr = 8
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [9, 14, 11, 18, 12, 11]
        self.modifiers = [-1, 2, 0, 4, 1, 0]
        self.proficiency = 3
        self.armor = 11
        self.hp = rd.randint(15, 120)
        self.dicecode = "15d8"
        self.saves = {"Int": 7, "Wis": 4}
        self.skills = {"Arcana": 7, "History": 7}
        self.senses = {"passive Perception": 11}
        self.languages = ["Common", "Draconic", "Elven", "Gnomish"]
        self.features = {
            "Portent": "When the diviner or a creature it can see makes an attack roll, a saving throw, or an ability check, the diviner can roll a d20 and choose to use this roll in place of the attack roll, saving throw, or ability check.",
            "Spellcasting": {
                "caster level": 15,
                "caster ability": "Intelligence",
                "spell save": 15,
                "spell attack": 7,
                "spell list": "wizard",
                "spellbook": {
                    "0": ["fire bolt", "light", "mage hand", "message", "true strike"],
                    "1": ["detect magic", "feather fall", "mage armor"],
                    "2": ["detect thoughts", "locate object", "scorching ray"],
                    "3": ["clairvoyance", "fly", "fireball"],
                    "4": ["arcane eye", "ice storm", "stoneskin"],
                    "5": ["Rary's telebathic band", "seeming"],
                    "6": ["mass suggestion", "true seeing"],
                    "7": ["delayed blast fireball", "teleport"],
                    "8": ["maze"]
                },
                "spell slots": {
                    "0": 0,
                    "1": 4,
                    "2": 3,
                    "3": 3,
                    "4": 3,
                    "5": 2,
                    "6": 1,
                    "7": 1,
                    "8": 1
                }
            }
        }
        self.actions = {
            "Quarterstaff": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[0]),
                "range": 5,
                "damage": self.find_damage(4, self.modifiers[0]),
                "damage code": '1d6 + {}'.format(self.modifiers[0]),
                "damage type": "bludgeoning"
            }
        }
        self.inventory = {}