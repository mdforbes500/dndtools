#!/usr/bin/python

import random
import math
import json

class NPC:
    """
    NPC: Contains a model of an NPC's basic statistics necessary for generating
    a stat block for it.
    """
    def __init__(self, name):
        """
        Constructor for NPC. Populates the character as a Commoner.
        """
        self.name = str(name)
        self.cr = 0
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(human)"
        self.alignment = "neutral"
        self.speed = 30
        self.abilities = [10,10,10,10,10,10]
        self.modifiers = [0,0,0,0,0,0]
        self.proficiency = 2
        self.armor = 10
        self.hp = 1
        self.dicecode = "1d6"
        self.skills = {'Medicine':4}
        self.senses = ["passive Perception 10"]
        self.languages = ["Common"]
        self.features = {}
        self.actions = {"Club":['Melee',2,5,1,'1d4','bludgeoning']}
        self.inventory = {}
        self.cast_level = 0
        self.caster = False
        self.cast_ability = ""
        self.cast_save = 0
        self.spell_attk = 0
        self.spell_list = ""
        self.spells = []
        self.slots = []

    def __del__(self):
        return None;

    #Methods
    def aarakocra(self):
        self.race = "(aarakocra)"
        self.abilities[1] += 2 # +2 to Dex
        self.abilities[4] += 2 # +2 to Wis

    def bullywug(self):
        self.race = "(bullywug)"
        self.abilities[3] -= 2 # -2 to Int
        self.abilities[5] -= 2 # -2 to Cha

    def dragonborn(self):
        self.race = "(dragonborn)"
        self.abilities[0] += 2 # +2 to Str
        self.abilities[5] += 1 # +1 to Cha

    def drow(self):
        self.race = "(elf)"
        self.abilities[1] += 2 # +2 to Dex
        self.abilities[5] += 1 # +1 to Cha

    def dwarf(self):
        self.race = "(dwarf)"
        roll = random.randint(1, 100)
        if roll >= 50:
            self.abilities[0] += 2 # +2 to Str
        else:
            self.abilities[4] += 2 # +2 to Wis
        self.abilities[2] += 2 # +2 to Con

    def elf(self):
        self.race = "(elf)"
        roll = random.randint(1, 100)
        if roll >= 50:
            self.abilities[3] += 1 # +1 to Int
        else:
            self.abilities[4] += 1 # +1 to Wis
        self.abilities[1] += 2 # +2 to Dex

    def gnoll(self):
        self.race = "(gnoll)"
        self.abilities[0] += 2 # +2 to Str
        self.abilities[3] -= 2 # -2 to Int

    def gnome(self):
        self.size = "Small"
        self.race = "(gnome)"
        roll = random.randint(1, 100)
        if roll >= 50:
            self.abilities[1] += 2 # +2 to Dex
        else:
            self.abilities[2] += 2 # +2 to Con
        self.abilities[3] += 2 # +2 to Int


    def deep_gnome(self):
        self.size = "Small"
        self.race = "(gnome)"
        self.abilities[0] += 1 # +1 to Str
        self.abilities[1] += 2 # +2 to Dex

    def goblin(self):
        self.size = "Small"
        self.race = "(goblinoid)"
        self.abilities[0] -= 2 # -2 to Str
        self.abilities[1] += 2 # +2 to Dex

    def grimlock(self):
        self.race = "(grimlock)"

    def half_elf(self):
        self.race = "(half-elf)"

    def half_orc(self):
        self.race = "(half-orc)"

    def halfling(self):
        self.size = "Small"
        self.race = "(halfling)"

    def hobgoblin(self):
        self.race = "(goblinoid)"

    def kenku(self):
        self.race = "(kenku)"

    def kobold(self):
        self.size = "Small"
        self.race = "(kobold)"

    def kuo_toa(self):
        self.race = "(kuo-toa)"

    def lizardfolk(self):
        self.race = "(lizardfolk)"

    def merfolk(self):
        self.race = "(merfolk)"

    def orc(self):
        self.race = "(orc)"

    def skeleton(self):
        self.type = "undead"
        self.race = None

    def tiefling(self):
        self.race = "(tiefling)"

    def troglodyte(self):
        self.race = "(troglodyte)"

    def zombie(self):
        self.type = "undead"
        self.race = None

    def export_json(self):
        dict = {
            "name": self.name,
            "cr": self.cr,
            "size": self.size,
            "type": self.type,
            "race": self.race,
            "alignment": self.alignment,
            "speed": self.speed,
            "abilities": [
                {"strength": self.abilities[0], "modifier": self.modifiers[0]},
                {"dexterity": self.abilities[1], "modifier": self.modifiers[1]},
                {"constitution": self.abilities[2], "modifier": self.modifiers[2]},
                {"intelligence": self.abilities[3], "modifier": self.modifiers[3]},
                {"wisdom": self.abilities[4], "modifier": self.modifiers[4]},
                {"charisma": self.abilities[5], "modifier": self.modifiers[5]}
            ],
            "proficiency": self.proficiency,
            "armor": self.armor,
            "hp": self.hp,
            "dicecode": self.dicecode,
            "skills": self.skills,
            "senses": self.senses,
            "languages": self.languages,
            "features": self.features,
            "actions": self.actions,
            "inventory": self.inventory,
            "cast_level": self.cast_level,
            "caster": self.caster,
            "cast_ability": self.cast_ability,
            "cast_save": self.cast_save,
            "spell_attk": self.spell_attk,
            "spell_list": self.spell_list,
            "spells": self.spells,
            "slots": self.slots
        }

        exported_json = json.dumps(dict)
        return exported_json
