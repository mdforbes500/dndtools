#!/usr/bin/python3

import random as rd
from . import npc

class Archdruid(npc.NPC):

    def __init__(self):
        super().__init__("Archdruid")
        self.cr = 12
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "human"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 15}
        self.abilities = [10, 14, 12, 12, 20, 11]
        self.modifiers = [0, 2, 1, 1, 5, 0]
        self.proficiency = 4
        self.armor = 16
        self.hp = rd.randint(48, 216)
        self.dicecode = "24d8 + 24"
        self.saves = {"Int": 5, "Wis": 9}
        self.skills = {"Medicine":9, "Nature":5, "Perception": 9}
        self.senses = {"passive Perception": 19}
        self.languages = ["Common", "Druidic", "Elven"]
        self.features = {
            "Spellcasting": {
                "caster level": 18,
                "caster ability": "Wisdom",
                "spell save": 17,
                "spell attack": 9,
                "spell list": "druid",
                "spellbook": {
                    "0": ["drudcraft", "mending", "poison spray", "produce flame"],
                    "1": ["cure wounds", "entangle", "faerie fire", "speak with animals"],
                    "2": ["animal messenger", "beast sense", "hold person"],
                    "3": ["conjure animals", "meld into stone", "water breathing"],
                    "4": ["dominate beast", "locate creature", "stoneskin", "wall of fire"],
                    "5": ["commune with nature", "mass cure wounds", "tree stride"],
                    "6": ["heal", "heroes' feast", "sunbeam"],
                    "7": ["fire storm"],
                    "8": ["animal shapes"],
                    "9": ["foresight"]
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
            "Scimitar": {
                "attack type": "Melee",
                "attack mod": self.find_attk_mod(self.modifiers[0]),
                "range": 5,
                "damage": self.find_damage(6, self.modifiers[0]),
                "damage code": '1d6 + {}'.format(self.modifiers[0]),
                "damage type": "slashing"
            },
            "Change Shape": "The archdruid magically polymorphs into a beast or elemental with a challenge rating of 6 or less, and can remain in this form for up to 9 hours. The archdruid can choose whether its equipment falls to the ground, melds with its new form, or is worn by the new form. The archdruid reverts to its true form if it dies or falls unconscious. The archdruid can revert to its true form using a bonus action on its turn. While in a new form, the archdruid retains its game statistics and ability to speak, but its AC, movement modes, Strength, and Dexterity are replaced by those of the new form, and it gains any special senses, proficiencies, traits, actions, and reactions (except class features, legendary actions, and lair actions) that the new form has but that it lacks. It can cast its spells with verbal or somatic components in its new form. The new form's attacks count as magical for the purpose of overcoming resistances and immunity to nonmagical attacks."
        }
        self.inventory = {}