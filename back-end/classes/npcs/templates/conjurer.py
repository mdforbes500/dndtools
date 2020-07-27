#!/usr/bin/python3

import random as rd
from . import npc

class Conjurer(npc.NPC):

    def __init__(self):
        super().__init__("Conjurer")
        self.cr = 6
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [9, 14, 11, 17, 12, 11]
        self.modifiers = [-1, 2, 0, 3, 1, 0]
        self.proficiency = 3
        self.armor = 12
        self.hp = rd.randint(9, 72)
        self.dicecode = "9d8"
        self.saves = {"Int": 6, "Wis": 4}
        self.skills = {"Arcana": 6, "History": 6}
        self.senses = {"passive Perception": 11}
        self.languages = ["Common", "Draconic", "Elven", "Gnomish"]
        self.features = {
            "Benign Transportation": "As a bonus action, the conjurer teleports up to 30 feet to an unoccupied space that it can see. If it instead chooses a space within range that is occupied by a willing Small or Medium creature, they both teleport, swapping places.",
            "Spellcasting": {
                "caster level": 9,
                "caster ability": "Intelligence",
                "spell save": 14,
                "spell attack": 6,
                "spell list": "wizard",
                "spellbook": {
                    "0": ["acid splash", "mage hand", "poison spray", "prestidigitation"],
                    "1": ["mage armor", "magic missile", "unseen servant"],
                    "2": ["cloud of daggers", "misty step", "web"],
                    "3": ["fireball", "stinking cloud"],
                    "4": ["Evard's black tantacles", "stoneskin"],
                    "5": ["cloudkill", "conjure elemental"]
                },
                "spell slots": {
                    "0": 0,
                    "1": 4,
                    "2": 3,
                    "3": 3,
                    "4": 3,
                    "5": 2
                }
            }
        }
        self.actions = {
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