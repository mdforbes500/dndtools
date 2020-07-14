#!/usr/bin/python3

import random as rd
from . import npc

class Archmage(npc.NPC):

    def __init__(self):
        super().__init__("Archmage")
        self.cr = 12
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [10, 14, 12, 20, 15, 16]
        self.modifiers = [0, 2, 1, 5, 2, 3]
        self.proficiency = 4
        self.armor = 12
        self.hp = rd.randint(36, 162)
        self.dicecode = "18d8 + 18"
        self.skills = {"Arcana":13, "History":13}
        self.senses = {"passive Perception": 12}
        self.resistance = ["damage from spells"]
        self.languages = ["Common", "Draconic", "Elven", "Infernal", "Abyssal", "Gnomish"]
        self.features = {
            "Magic Resistance": "The archmage has advantage on saving throws against spells and other magical effects",
            "Spellcasting": {
                "caster level": 18,
                "caster ability": "Intelligence",
                "spell save": 17,
                "spell attack": 9,
                "spell list": "wizard",
                "spellbook": {
                    "0": ["fire bolt", "mage hand", "prestidigitation", "shocking grasp"],
                    "1": ["detect magic", "identify", "mage armor", "magic missile"],
                    "2": ["detect thoughts", "mirror image", "misty step"],
                    "3": ["counterspell", "fly", "lightning bolt"],
                    "4": ["banishment", "fire shield", "stoneskin"],
                    "5": ["cone of cold", "scrying", "wall of force"],
                    "6": ["globe of invisibility"],
                    "7": ["teleport"],
                    "8": ["mind blank"],
                    "9": ["time stop"]
                },
                "spell slots": {
                    "0": 0,
                    "1": 4,
                    "2": 3,
                    "3": 3,
                    "4": 3,
                    "5": 3,
                    "6": 1,
                    "7": 1,
                    "8": 1,
                    "9": 1
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