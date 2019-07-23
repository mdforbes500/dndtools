#!/usr/bin/env bash

import random

class Building:
    """
    Building class for D&D settlement generation. Randomly generates a
    building's type and details for the Settelment class' generator.
    """
    def __init__(self):
        self.type = ""
        self.details = ""

        # Roll the building's type
        roll = random.randint(1, 20)

        if roll <= 10:
            self.type = "Residence"

            # Roll details for residences
            roll = random.randint(1, 20)
            if roll <= 2:
                self.details = "Abandoned Squat"
            elif roll > 2 and roll <= 8:
                self.details = "Middle-class home"
            elif roll > 8 and roll <= 10:
                self.details = "Upper-class home"
            elif roll > 10 and roll <= 15:
                self.details = "Crowded tenement"
            elif roll > 15 and roll <= 17:
                self.details = "Orphanage"
            elif roll is 18:
                self.details = "Hidden slaver's den"
            elif roll is 19:
                self.details = "Front for a secret cult"
            else:
                self.details = "Lavish, guarded mansion"

        # Religious building
        elif roll > 10 and roll <= 12:
            self.type = "Religious building"

            # Roll details for religious buildings
            roll = random.randint(1, 20)
            if roll <= 10:
                self.details = "Temple to a good or neutral deity"
            elif roll > 10 and roll <= 12:
                self.details = "Temple to a false deity (run by charlatan priests"
            elif roll is 13:
                self.details = "Home of ascetics"
            elif roll > 13 and roll <= 15:
                self.details = "Abandeoned shrine"
            elif roll > 15 and roll <= 17:
                self.details = "Library dedicated to religious study"
            else:
                self.details = "Hidden shrine to a fiend or evil deity"

            # Tavern
        elif roll > 12 and roll <=15:
            # Create Tavern Name
            firstpart = ""
            secondpart = ""

            roll = random.randint(1, 20)
            if roll is 1:
                firstpart = "The Silver"
            elif roll is 2:
                firstpart = "The Golden"
            elif roll is 3:
                firstpart = "The Staggering"
            elif roll is 4:
                firstpart = "The Laughing"
            elif roll is 5:
                firstpart = "The Prancing"
            elif roll is 6:
                firstpart = "The Gilded"
            elif roll is 7:
                firstpart = "The Running"
            elif roll is 8:
                firstpart = "The Howling"
            elif roll is 9:
                firstpart = "The Slaughtered"
            elif roll is 10:
                firstpart = "The Leering"
            elif roll is 11:
                firstpart = "The Drunken"
            elif roll is 12:
                firstpart = "The Leaping"
            elif roll is 13:
                firstpart = "The Roaring"
            elif roll is 14:
                firstpart = "The Frowning"
            elif roll is 15:
                firstpart = "The Lonely"
            elif roll is 16:
                firstpart = "The Wandering"
            elif roll is 17:
                firstpart = "The Mysterious"
            elif roll is 18:
                firstpart = "The Barking"
            elif roll is 19:
                firstpart = "The Black"
            else:
                firstpart = "The Gleaming"

            roll = random.randint(1, 20)
            if roll is 1:
                secondpart = "Eel"
            elif roll is 2:
                secondpart = "Dolphin"
            elif roll is 3:
                secondpart = "Dwarf"
            elif roll is 4:
                secondpart = "Pegasus"
            elif roll is 5:
                secondpart = "Pony"
            elif roll is 6:
                secondpart = "Rose"
            elif roll is 7:
                secondpart = "Stag"
            elif roll is 8:
                secondpart = "Wolf"
            elif roll is 9:
                secondpart = "Lamb"
            elif roll is 10:
                secondpart = "Demon"
            elif roll is 11:
                secondpart = "Goat"
            elif roll is 12:
                secondpart = "Spirit"
            elif roll is 13:
                secondpart = "Horde"
            elif roll is 14:
                secondpart = "Jester"
            elif roll is 15:
                secondpart = "Mountain"
            elif roll is 16:
                secondpart = "Eagle"
            elif roll is 17:
                secondpart = "Satyr"
            elif roll is 18:
                secondpart = "Dog"
            elif roll is 19:
                secondpart = "Spider"
            else:
                secondpart = "Star"

            tavernname = firstpart + " " + secondpart
            self.type = "Tavern: " + tavernname

            # Roll details for taverns
            roll = random.randint(1, 20)
            if roll < 5:
                self.details = "Quiet, low-key bar"
            elif roll > 5 and roll <= 9:
                self.details = "Raucous dive"
            elif roll is 10:
                self.details = "Thieves' guild hangout"
            elif roll is 11:
                self.details = "Gathering place for a secret society"
            elif roll > 11 and roll <= 13:
                self.details = "Upper-class dining club"
            elif roll > 13 and roll <= 15:
                self.details = "Gambling den"
            elif roll > 15 and roll <= 17:
                self.details = "Caters to specific race or guild"
            elif roll is 18:
                self.details = "Members-only club"
            else:
                self.details = "Brothel"

        # Warehouses
        elif roll > 15 and roll <= 17:
            self.type = "Warehouse"

            # Roll details for warehouses
            roll = random.randint(1, 20)
            if roll < 4:
                self.details = "Empty or abandoned"
            elif roll > 4 and roll <= 6:
                self.details = "Heavily guarded, expensive goods"
            elif roll > 6 and roll <= 10:
                self.details = "Cheap goods"
            elif roll > 10 and roll <= 14:
                self.details = "Bulk goods"
            elif roll is 15:
                self.details = "Live animals"
            elif roll > 15 and roll <= 17:
                self.details = "Weapons/armor"
            elif roll > 17 and roll <= 19:
                self.details = "Goods from a distant land"
            else:
                self.details = "Secret smuggler's den"

        # Shops
        else:
            self.type = "Shop"

            # Roll details for shops
            roll = random.randint(1, 20)
            if roll is 1:
                self.details = "Pawnshop"
            elif roll is 2:
                self.details = "Herbs/incense"
            elif roll is 3:
                self.details = "Fruits/vegetables"
            elif roll is 4:
                self.details = "Dried meats"
            elif roll is 5:
                self.details = "Pottery"
            elif roll is 6:
                self.details = "Undertaker"
            elif roll is 7:
                self.details = "Books"
            elif roll is 8:
                self.details = "Moneylender"
            elif roll is 9:
                self.details = "Weapons/armor"
            elif roll is 10:
                self.details = "Chandler"
            elif roll is 11:
                self.details = "Smithy"
            elif roll is 12:
                self.details = "Carpenter"
            elif roll is 13:
                self.details = "Weaver"
            elif roll is 14:
                self.details = "Jeweler"
            elif roll is 15:
                self.details = "Baker"
            elif roll is 16:
                self.details = "Mapmaker"
            elif roll is 17:
                self.details = "Tailor"
            elif roll is 18:
                self.details = "Ropemaker"
            elif roll is 18:
                self.details = "Mason"
            else:
                self.details = "Scribe"
#end of class
