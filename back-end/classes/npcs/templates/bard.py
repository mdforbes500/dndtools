#!/usr/bin/python3

import random as rd
from . import npc

class Acolyte(npc.NPC):

    def __init__(self):
        super().__init__("Bard")
        self.cr = 2
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [11, 14, 12, 10, 13, 14]
        self.modifiers = [0, 2, 1, 0, 1, 2]
        self.proficiency = 2
        self.armor = 15
        self.hp = rd.randint(16, 72)
        self.dicecode = "8d8+8"
        self.saves = {"Dex": 4, "Wis": 3}
        self.skills = {"Acrobatics": 4, "Perception": 5, "Performance": 6}
        self.senses = {"passive Perception": 15}
        self.languages = ["Common", "Elvish"]
        self.features = {
            "Song of Rest": "The bard can perform a song while taking a short rest. Any ally who hears the song regains an extra 1d6 hit points if it spends any Hit Dice to regain hit points at the end of that rest. The bard can confer this benefit on itself as well.",
            "Spellcasting": {
                "caster level": 4,
                "caster ability": "Charisma",
                "spell save": 12,
                "spell attack": 4,
                "spell list": "bard",
                "spellbook": {
                    "0": ["friends", "mage hand", "vicious mockery"],
                    "1": ["charm person", "healing word", "heroism", "sleep", "thunderwave"],
                    "2": ["invisibility", "shatter"]
                },
                "spell slots": {
                    "0": 0,
                    "1": 4,
                    "2": 3
                }
            },
            "Taunt": "The bard can use a bonus action on its turn to target one creature within 30 feet of it. If the target can hear the bard, the target must succeed on a DC 12 Charisma saving throw or have disadvantage on ability checks, attack rolls, and saving throws until the start of the bard's next turn."
        }
        self.actions = {
            "Shortsword": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[0]),
                "range": 5,
                "damage": self.find_damage(6, self.modifiers[0]),
                "damage code": '1d6 + {}'.format(self.modifiers[0]),
                "damage type": "piercing"
            },
            "Shortbow": {
                "attack type": "Ranged",
                "attack mod": self.find_attk_mod(self.modifiers[1]),
                "range": 320,
                "damage": self.find_damage(6, self.modifiers[1]),
                "damage code": '1d6 + {}'.format(self.modifiers[1]),
                "damage type": "piercing"
            }
        }
        self.inventory = {}