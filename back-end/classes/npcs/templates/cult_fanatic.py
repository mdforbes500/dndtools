#!/usr/bin/python3

import random as rd
from . import npc

class CultFanatic(npc.NPC):

    def __init__(self):
        super().__init__("Cult Fanatic")
        self.cr = 2
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [11, 14, 12, 10, 13, 14]
        self.modifiers = [0, 2, 1, 0, 1, 2]
        self.proficiency = 2
        self.armor = 13
        self.hp = rd.randint(12, 54)
        self.dicecode = "6d8 + 6"
        self.skills = {"Deception": 4, "Persuasion": 4, "Religion": 2}
        self.senses = {"passive Perception": 11}
        self.languages = ["Common"]
        self.features = {
            "Dark Devotion": "The fanatic has advantage on saving throws against being charmed or frightened.",
            "Spellcasting": {
                "caster level": 4,
                "caster ability": "Wisdom",
                "spell save": 11,
                "spell attack": 3,
                "spell list": "cleric",
                "spellbook": {
                    "0": ["light", "sacred flame", "thaumaturgy"],
                    "1": ["command", "inflict wounds", "shield of faith"],
                    "2": ["hold person", "spiritual weapon"]
                },
                "spell slots": {
                    "0": 0,
                    "1": 4,
                    "2": 3
                }
            }
        }
        self.actions = {
            "Multiattack": "The fanatic makes two melee attacks.",
            "Dagger": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[1]),
                "range": 5,
                "damage": self.find_damage(4, self.modifiers[0]),
                "damage code": '1d4 + {}'.format(self.modifiers[0]),
                "damage type": "piercing"
            }
        }
        self.inventory = {}