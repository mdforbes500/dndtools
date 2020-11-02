#!/usr/bin/python
import random
import classes.npc as npc

def dragonborn(obj):
    obj.race = "(dragonborn)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[5] += 1 # +1 to Cha

def drow(obj):
    obj.race = "(elf)"
    obj.abilities[1] += 2 # +2 to Dex
    obj.abilities[5] += 1 # +1 to Cha

def hill_dwarf(obj):
    obj.race = "(dwarf)"
    obj.abilities[4] += 2 # +2 to Wis
    obj.abilities[2] += 2 # +2 to Con

def mountain_dwarf(obj):
    obj.race = "(dwarf)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[2] += 2 # +2 to Con

def wood_elf(obj):
    obj.race = "(elf)"
    obj.abilities[4] += 1 # +1 to Wis
    obj.abilities[1] += 2 # +2 to Dex

def high_elf(obj):
    obj.race = "(elf)"
    obj.abilities[3] += 1 # +1 to Int
    obj.abilities[1] += 2 # +2 to Dex

def gnoll(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(gnoll)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[3] -= 2 # -2 to Int
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Rampage"] = "When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack."
    obj.senses["darkvision"] = 60

def rock_gnome(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(gnome)"
    obj.abilities[2] += 2 # +2 to Con
    obj.abilities[3] += 2 # +2 to Int

def forest_gnome(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(gnome)"
    obj.abilities[1] += 2 # +2 to Dex
    obj.abilities[3] += 2 # +2 to Int

def deep_gnome(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(gnome)"
    obj.abilities[0] += 1 # +1 to Str
    obj.abilities[1] += 2 # +2 to Dex
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Gnome Cunning"] = "The gnome has advantage on Intelligence, Widsom and Charisma saving throws against magic."
    obj.features["Innate Spellcasting"] = "The gnome's innate spellcasting ability is Intelligence (spell save DC {}). It can innately cast the following spells, requiring no material components:\n\nAt will: <i>nondetection</i> (self only)\n1/day each: <i>blindness/deafness, blur, disguise self</i>".format(8 + obj.proficiency + obj.modifiers[3])
    obj.features["Stone Camouflage"] = "The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
    obj.speed["ground"] = 20
    obj.senses["darkvision"] = 120
    obj.langauges.append("Gnomish")
    obj.langauges.append("Terran")
    obj.langauges.append("Undercommon")

def goblin(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(goblinoid)"
    obj.abilities[0] -= 2 # -2 to Str
    obj.abilities[1] += 2 # +2 to Dex
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Nimble Escape"] = "The goblin can take the Disengage or Hide action as a bonus action on each of its turns."
    obj.senses["darkvision"] = 60
    obj.languages.append("Goblin")

def grimlock(obj):
    obj.race = "(grimlock)"

def half_elf(obj):
    obj.race = "(half-elf)"

def half_orc(obj):
    obj.race = "(half-orc)"

def halfling(obj):
    obj.size = "Small"
    obj.race = "(halfling)"

def hobgoblin(obj):
    obj.race = "(goblinoid)"

def kenku(obj):
    obj.race = "(kenku)"

def kobold(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(kobold)"

def kuo_toa(obj):
    obj.race = "(kuo-toa)"

def lizardfolk(obj):
    obj.race = "(lizardfolk)"

def merfolk(obj):
    obj.race = "(merfolk)"

def orc(obj):
    obj.race = "(orc)"

def skeleton(obj):
    obj.type = "undead"
    obj.race = None

def tiefling(obj):
    obj.race = "(tiefling)"

def troglodyte(obj):
    obj.race = "(troglodyte)"

def zombie(obj):
    obj.type = "undead"
    obj.race = None
