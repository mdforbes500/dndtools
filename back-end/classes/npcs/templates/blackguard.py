#!/usr/bin/python3

import random as rd
from . import npc

class Blackguard(npc.NPC):
    """
    Commoner NPC template data model derived from the NPC super.
    """
    def __init__(self) -> None:
        super().__init__("Blackguard")
        self.cr = 8
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [18,11,18,11,14,15]
        self.modifiers = [4,0,4,0,2,2]
        self.proficiency = 3
        self.armor = 18
        self.hp = rd.randint(98,216)
        self.dicecode = "18d8 + 72"
        self.saves = {"Wis": 5, "Cha": 5}
        self.senses = {"passive Perception": 12}
        self.languages = ["Common"]
        self.features = {
            "Spellcasting": {
                "caster level": 10,
                "caster ability": "Charisma",
                "spell save": 13,
                "spell attack": 5,
                "spell list": "paladin",
                "spellbook": {
                    "1": ["command", "protection from evil and good", "thunderous smite"],
                    "2": ["branding smite", "find steed"],
                    "3": ["blinding smite", "dispel magic"]
                },
                "spell slots": {
                    "1": 4,
                    "2": 3,
                    "3": 2
                }
            }
        }
        self.actions = {
            "Multiattack": "The blackguard makes three attacks with its glaive or its shortbow.",
            "Glaive": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[0]),
                "range": 10,
                "damage": self.find_damage(10, self.modifiers[0]),
                "damage code": '1d10 + {}'.format(self.modifiers[0]),
                "damage type": "slashing"
            },
            "Shortbow": {
                "attack type": "Ranged",
                "attack mod": self.find_attk_mod(self.modifiers[1]),
                "range": 320,
                "damage": self.find_damage(6, self.modifiers[1]),
                "damage code": '1d6 + {}'.format(self.modifiers[1]),
                "damage type": "piercing"
            },
            "Dereadful Aspect": "The blackguard exudes magical menace. Each enemy within 30 feet of the blackguard must succeed on a DC 13 Wisdom saving throw or be frightened for 1 minute. If a frightened target ends its turn more than 30 feet away from the blackguard, the target can repeat the saving throw, ending the effect on itself on a success."
        }
        self.inventory = {}
