#!/usr/bin/python3

import random as rd
from . import npc

class Abjurer(npc.NPC):

    def __init__(self):
        super().__init__("Abjurer")
        self.cr = 9
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [9, 14, 14, 18, 12, 11]
        self.modifiers = [-1, 2, 2, 4, 1, 0]
        self.proficiency = 4
        self.armor = 12
        self.hp = rd.randint(39, 130)
        self.dicecode = "13d8 + 26"
        self.saves = {"Int": 8, "Wis": 5}
        self.skills = {"Arcana":8, "History":8}
        self.senses = {"passive Perception": 11}
        self.languages = ["Common", "Draconic", "Elven", "Gnomish"]
        self.features = {
            "Arcane Ward": "The abjurer has a magical ward that has 30 hit points. Whenever the abjurer takes damage, the ward takes the damage instead. If the ward is reduced to 0 hit points, the abjurer takes any remaining damage. When the abjurer casts an abjuration spell of 1st level or higher, the ward regains a number of hit points equal to twice the level of the spell.",
            "Spellcasting": {
                "caster level": 13,
                "caster ability": "Intelligence",
                "spell save": 16,
                "spell attack": 8,
                "spell list": "wizard",
                "spellbook": {
                    "0": ["blade ward", "dancing lights", "mending", "message", "ray of frost"],
                    "1": ["alarm", "mage armor", "magic missile", "shield"],
                    "2": ["arcane lock", "invisibility"],
                    "3": ["counterspell", "dispel magic", "fireball"],
                    "4": ["banishment", "stoneskin"],
                    "5": ["cone of cold", "wall of force"],
                    "6": ["flesh to stone", "globe of invisibility"],
                    "7": ["symbol", "teleport"],
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