#!/usr/bin/python3

import random as rd
from . import npc

class ApprenticeWizard(npc.NPC):

    def __init__(self):
        super().__init__("Apprentice Wizard")
        self.cr = 0.25
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [10, 10, 10, 14, 10, 11]
        self.modifiers = [0, 0, 0, 2, 0, 0]
        self.proficiency = 2
        self.armor = 10
        self.hp = rd.randint(2, 16)
        self.dicecode = "2d8"
        self.skills = {"Arcana":4, "History":4}
        self.senses = {"passive Perception": 10}
        self.languages = ["Common"]
        self.features = {
            "Spellcasting": {
                "caster level": 1,
                "caster ability": "Intelligence",
                "spell save": 12,
                "spell attack": 4,
                "spell list": "wizard",
                "spellbook": {
                    "0": ["fire bolt", "mending", "prestidigitation"],
                    "1": ["burning hands", "disguise self", "shield"]
                },
                "spell slots": {
                    "0": 0,
                    "1": 2
                }
            }
        }
        self.actions = {
            "Dagger": {
                "attack type": "Melee or Ranged",
                "attack mod": self.find_attk_mod(self.modifiers[0]),
                "range": 5,
                "damage": self.find_damage(4, self.modifiers[0]),
                "damage code": '1d4 + {}'.format(self.modifiers[0]),
                "damage type": "piercing"
            }
        }
        self.inventory = {}