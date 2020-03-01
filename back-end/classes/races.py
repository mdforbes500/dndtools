#!/usr/bin/python
import random

def aarakocra(obj):
    obj.race = "(aarakocra)"
    obj.abilities[1] += 2 # +2 to Dex
    obj.abilities[4] += 2 # +2 to Wis

def bullywug(obj):
    obj.race = "(bullywug)"
    obj.abilities[3] -= 2 # -2 to Int
    obj.abilities[5] -= 2 # -2 to Cha

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
    obj.race = "(gnoll)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[3] -= 2 # -2 to Int

def rock_gnome(obj):
    obj.size = "Small"
    obj.race = "(gnome)"
    obj.abilities[2] += 2 # +2 to Con
    obj.abilities[3] += 2 # +2 to Int

def forest_gnome(obj):
    obj.size = "Small"
    obj.race = "(gnome)"
    obj.abilities[1] += 2 # +2 to Dex
    obj.abilities[3] += 2 # +2 to Int


def deep_gnome(obj):
    obj.size = "Small"
    obj.race = "(gnome)"
    obj.abilities[0] += 1 # +1 to Str
    obj.abilities[1] += 2 # +2 to Dex

def goblin(obj):
    obj.size = "Small"
    obj.race = "(goblinoid)"
    obj.abilities[0] -= 2 # -2 to Str
    obj.abilities[1] += 2 # +2 to Dex

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
