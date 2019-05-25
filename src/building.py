import random

class Building:

    def __init__(self):
        self.type = ''
        self.details = ''

        # Roll the building's type
        roll = random.randint(1,20)

        if roll <= 10:
            self.type = "Residence"

            # Roll details for residences
            roll = random.randint(1,20)
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
            elif roll == 18:
                self.details = "Hidden slaver's den"
            elif roll == 19:
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
            elif roll == 13:
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
            if roll == 1:
                firstpart = "The Silver"
            elif roll == 2:
                firstpart = "The Golden"
            elif roll == 3:
                firstpart = "The Staggering"
            elif roll == 4:
                firstpart = "The Laughing"
            elif roll == 5:
                firstpart = "The Prancing"
            elif roll == 6:
                firstpart = "The Gilded"
            elif roll == 7:
                firstpart = "The Running"
            elif roll == 8:
                firstpart = "The Howling"
            elif roll == 9:
                firstpart = "The Slaughtered"
            elif roll == 10:
                firstpart = "The Leering"
            elif roll == 11:
                firstpart = "The Drunken"
            elif roll == 12:
                firstpart = "The Leaping"
            elif roll == 13:
                firstpart = "The Roaring"
            elif roll == 14:
                firstpart = "The Frowning"
            elif roll == 15:
                firstpart = "The Lonely"
            elif roll == 16:
                firstpart = "The Wandering"
            elif roll == 17:
                firstpart = "The Mysterious"
            elif roll == 18:
                firstpart = "The Barking"
            elif roll == 19:
                firstpart = "The Black"
            else:
                firstpart = "The Gleaming"

            roll = random.randint(1, 20)
            if roll == 1:
                secondpart = "Eel"
            elif roll == 2:
                secondpart = "Dolphin"
            elif roll == 3:
                secondpart = "Dwarf"
            elif roll == 4:
                secondpart = "Pegasus"
            elif roll == 5:
                secondpart = "Pony"
            elif roll == 6:
                secondpart = "Rose"
            elif roll == 7:
                secondpart = "Stag"
            elif roll == 8:
                secondpart = "Wolf"
            elif roll == 9:
                secondpart = "Lamb"
            elif roll == 10:
                secondpart = "Demon"
            elif roll == 11:
                secondpart = "Goat"
            elif roll == 12:
                secondpart = "Spirit"
            elif roll == 13:
                secondpart = "Horde"
            elif roll == 14:
                secondpart = "Jester"
            elif roll == 15:
                secondpart = "Mountain"
            elif roll == 16:
                secondpart = "Eagle"
            elif roll == 17:
                secondpart = "Satyr"
            elif roll == 18:
                secondpart = "Dog"
            elif roll == 19:
                secondpart = "Spider"
            else:
                secondpart = "Star";

            tavernname = firstpart + " " + secondpart;
            self.type = "Tavern: " + tavernname;

            #Roll details for taverns
            roll = random.randint(1, 20)
            if roll < 5:
                self.details = "Quiet, low-key bar"
            elif roll > 5 and roll <= 9:
                self.details = "Raucous dive"
            elif roll == 10:
                self.details = "Thieves' guild hangout"
            elif roll == 11:
                self.details = "Gathering place for a secret society"
            elif roll > 11 and roll <= 13:
                self.details = "Upper-class dining club"
            elif roll > 13 and roll <= 15:
                self.details = "Gambling den"
            elif roll > 15 and roll <= 17:
                self.details = "Caters to specific race or guild"
            elif roll == 18:
                self.details = "Members-only club"
            else:
                self.details = "Brothel"

        #Warehouses
        elif roll > 15 and roll <= 17:
            #building = Building();      # Remove if not playing CoS

            #---- UNCOMMENT IF NOT PLAYING COS ----#
            self.type = "Warehouse"

            # Roll dtails for warehouses
            roll = random.randint(1, 20)
            if roll < 4:
                self.details = "Empty or abandoned"
            elif roll > 4 and roll <= 6:
                self.details = "Heavily guarded, expensive goods"
            elif roll > 6 and roll <= 10:
                self.details = "Cheap goods"
            elif roll > 10 and roll <= 14:
                self.details = "Bulk goods"
            elif roll == 15:
                self.details = "Live animals"
            elif roll > 15 and roll <= 17:
                self.details = "Weapons/armor"
            elif roll > 17 and roll <= 19:
                self.details = "Goods from a distant land"
            else:
                self.details = "Secret smuggler's den"

        # Shops
        else:
            #building = Building();      #Remove if not playing CoS

            #---- UNCOMMENT IF NOT PLAYING COS ----#
            self.type = "Shop"

            # Roll details for shops
            roll = random.randint(1, 20)
            if roll == 1:
                self.details = "Pawnshop"
            elif roll == 2:
                self.details = "Herbs/incense"
            elif roll == 3:
                self.details = "Fruits/vegetables"
            elif roll == 4:
                self.details = "Dried meats"
            elif roll == 5:
                self.details = "Pottery"
            elif roll == 6:
                self.details = "Undertaker"
            elif roll == 7:
                self.details = "Books"
            elif roll == 8:
                self.details = "Moneylender"
            elif roll == 9:
                self.details = "Weapons/armor"
            elif roll == 10:
                self.details = "Chandler"
            elif roll == 11:
                self.details = "Smithy"
            elif roll == 12:
                self.details = "Carpenter"
            elif roll == 13:
                self.details = "Weaver"
            elif roll == 14:
                self.details = "Jeweler"
            elif roll == 15:
                self.details = "Baker"
            elif roll == 16:
                self.details = "Mapmaker"
            elif roll == 17:
                self.details = "Tailor"
            elif roll == 18:
                self.details = "Ropemaker"
            elif roll == 18:
                self.details = "Mason"
            else:
                self.details = "Scribe"
