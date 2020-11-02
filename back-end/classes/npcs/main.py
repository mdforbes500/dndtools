#!/usr/bin/python3

from . import npc
from . import races

#set script variables
prodecural = True

def main(race, template, prodecural=True, **kwargs):
    #step 1: set name
    character = npc.NPC(set_name(race))

    #step 2: set size
    

def set_name(race, procedural=True, **kwargs):
    if procedural is False:
        name = input("Please enter a name:\n")
        print(f'You entered {name}')
    else:
        name = lookup_name(race)
    return name

def lookup_name(race):
    name = None
    return name

def set_size(race, npc, **kwargs):
    #revise race module as a system of classes
    pass 