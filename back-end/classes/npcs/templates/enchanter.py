#!/usr/bin/python3

import random as rd
from . import npc

class Enchanter(npc.NPC):

    def __init__(self):
        super().__init__("Enchanter")
        self.cr = 3
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [9, 14, 11, 17, 12, 11]
        self.modifiers = [-1, 2, 1, 3, 0, 1]
        self.proficiency = 2
        self.armor = 12
        self.hp = rd.randint(9, 72)
        self.dicecode = "9d8"
        self.saves = {"Int": 6, "Wis": 4}
        self.skills = {"Arcana": 6, "History": 6}
        self.senses = {"passive Perception": 11}
        self.languages = ["Common", "Draconic", "Elven", "Gnomish"]
        self.features = {
            "Spellcasting": {
                "caster level": 9,
                "caster ability": "Intelligence",
                "spell save": 14,
                "spell attack": 6,
                "spell list": "wizard",
                "spellbook": {
                    "0": ["friends", "mage hand", "mending", "message"],
                    "1": ["charm person", "magic missile", "mage armor"],
                    "2": ["hold person", "invisibility", "suggestion"],
                    "3": ["fireball", "haste", "tongues"],
                    "4": ["dominate beast", "stoneskin"],
                    "5": ["hold monster"],
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
            "Quarterstaff": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[0]),
                "range": 5,
                "damage": self.find_damage(4, self.modifiers[0]),
                "damage code": '1d6 + {}'.format(self.modifiers[0]),
                "damage type": "bludgeoning"
            }
        }
        self.reactions = {
            "Instinctive Charm": "The enchanter tries to magically divert an attack made against it, provided that the attacker is within 30 feet of it and visible to it. The enchanter must decide to do so before the attack hits or misses.\nThe attacker must make a DC 14 Wisdom saving throw. On a failed save, the attacker targets the creature closest to it, other than the enchanter or itself. If multiple creatures are closest, the attacker chooses which one to target."
        }
        self.inventory = {}