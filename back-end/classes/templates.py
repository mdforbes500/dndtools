#!/usr/bin/python

import random as rd
from . import npc

class Acolyte(npc.NPC):

    def __init__(self):
        super().__init__("Acolyte")
        self.cr = 0.25
        self.abilities = [10, 10, 10, 10, 14, 11]
        self.modifiers = [0, 0, 0, 0, 2, 0]
        self.hp = rd.randint(2, 16)
        self.dicecode = "2d8"
        self.skills = {"Medicine":4, "Religion":2}
        self.senses = ["passive perception 12"]
        self.languages = ["Common"]
        self.features = ["spellcasting"]
        self.inventory = {}
        self.cast_level = 1
        self.caster = True
        self.cast_ability = "Wisdom"
        self.cast_save = 12
        self.spell_attk = 4
        self.spell_list = "cleric"
        self.spells = [["light", "sacred flame", "thaumaturgy"],["bless", "cure wounds", "sanctuary"]]
        self.slots = [0, 3]
