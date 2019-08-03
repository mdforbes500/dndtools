#!/usr/bin/env python

import building as bldg
import random
from math import floor

class Settlement:
    """
    Settlement class creates a D&D settlement based upon integer RNGs.
    """

    def __init__(self, name, type):
        """
        Constructor for Settlement class. All values are empty prior to
        mutation by associated methods. Takes two inputs: the name as a string,
        and the type as a string.
        """
        self.name = name
        self.type = type

        #Statistics
        self.size = None
        self.population = None

        # Commerce
        self.gplimit = None
        self.wealth = None

        # Politics
        self.powermod = None
        self.powerctrs = None
        self.government = None
        self.relations = None
        self.status = None

        # Details
        self.traits = None
        self.knownfor = None
        self.calamity = None
        self.buildings = None
        self.npcs = None

        # Populate & parse
        self.set_size()
        self.set_powerctrs()
        self.set_government()
        self.set_relations()
        self.set_status()
        self.set_traits()
        self.set_knownfor()
        self.set_calamity()
        self.set_buildings()

    # Determine size and associated statistics
    def set_size(self):
        """
        Set_size is a mutator method for the Settlement Class that randomly
        generates a settlement of various size based on RNG integer values.
        In addition, it gives ome related statistics of population, gold piece
        limit for the community, and a modifier for power center generation.
        Finally, it generates the wealth of the community in gold pieces and
        stores it.
        """
        # Roll a d100
        roll = random.randint(1, 100)

        # Table 5-2 for Human Settlements, DMG1 (3.5e), pg. 137
        if roll <= 10:
            self.size = "Thorp"
            self.population = random.randint(20, 80)
            self.gplimit = 40    #gp
            self.powermod = -1
        elif roll > 10 and roll <= 30:
            self.size = "Hamlet"
            self.population = random.randint(81, 400)
            self.gplimit = 100   #gp
            self.powermod = 0
        elif roll > 30 and roll <= 50:
            self.size = "Village"
            self.population = random.randint(401, 900)
            self.gplimit = 200   #gp
            self.powermod = 1
        elif roll > 50 and roll <= 70:
            self.size = "Small Town"
            self.population = random.randint(901, 2000)
            self.gplimit = 200   #gp
            self.powermod = 2
        elif roll > 70 and roll <= 85:
            self.size = "Large Town"
            self.population = random.randint(2001, 5000)
            self.gplimit = 800   #gp
            self.powermod = 3
        elif roll > 85 and roll <= 95:
            self.size = "Small City"
            self.population = random.randint(5001, 12000)
            self.gplimit = 15000   #gp
            self.powermod = 4
        elif roll > 95 and roll <= 99:
            self.size = "Large City"
            self.population = random.randint(12001, 25000)
            self.gplimit = 40000   #gp
            self.powermod = 5
        else:
            self.size = "Metropolis"
            self.population = random.randint(25001, 1000000)
            self.gplimit = 100000  #gp
            self.powermod = 6

        # Determine community wealth on hand, DMG1 (3.5e) pg. 137
        self.wealth = 0.5*self.gplimit + 0.1*self.population

    def set_powerctrs(self):
        """
        Set_powerctrs is a mutator method for the Settlement class. Determines
        a multi-dimensional array of power centers for the city, with associated
        alignments.
        """
        self.powerctrs = []

        # Determine number of power centers, DMG1 (3.5e) pg. 137
        if self.size is "Small City":
            rerolls = 2
        elif self.size is "Large City":
            rerolls = 3
        elif self.size is "Metropolis":
            rerolls = 4
        else:
            rerolls = 1

        # Power Center Types, DMG1 (3.5e) pg. 137
        for i in range(rerolls):
            roll = random.randint(1, 20) + self.powermod
            if roll <= 13:
                self.powerctrs.append(["Conventional"])
                mroll = random.randint(1, 100)
                if mroll >= 95:
                    self.powerctrs.append(["Monstrous"])
            elif roll > 13 and roll <= 18:
                self.powerctrs.append(["Nonstandard"])
            else:
                self.powerctrs.append(["Magical"])

        # Power Center Alignments, DMG1 (3.5e) pg. 138
        for i in range(len(self.powerctrs)):
            roll = random.randint(1,100)
            if roll <= 35:
                self.powerctrs[i].append("Lawful good")
            elif roll >36 and roll <= 39:
                self.powerctrs[i].append("Neutral good")
            elif roll >40 and roll <= 41:
                self.powerctrs[i].append("Chaotic good")
            elif roll >42 and roll <= 61:
                self.powerctrs[i].append("Lawful neutral")
            elif roll >62 and roll <= 63:
                self.powerctrs[i].append("Neutral")
            elif roll is 64:
                self.powerctrs[i].append("Chaotic Neutral")
            elif roll >65 and roll <= 90:
                self.powerctrs[i].append("Lawful evil")
            elif roll >91 and roll <= 98:
                self.powerctrs[i].append("Neutral evil")
            else:
                self.powerctrs[i].append("Chaotic evil")

    def set_government(self):
        """
        Set_government is a mutator method for the Settlement class. Determines
        the government of the settlement by integer RNG.
        """
        # Roll d100
        roll = random.randint(1, 100)

        # Forms of Government, DMG (5e) pg. 18
        if roll <= 8:
            self.government = "Autocracy"
        elif roll > 8 and roll <= 13:
            self.government = "Bureaucracy"
        elif roll > 13 and roll <= 19:
            self.government = "Confederacy"
        elif roll > 19 and roll <= 22:
            self.government = "Democracy"
        elif roll > 22 and roll <= 27:
            self.government = "Dictatorship"
        elif roll > 27 and roll <= 42:
            self.government = "Feudalism"
        elif roll > 42 and roll <= 44:
            self.government = "Gerontocracy"
        elif roll > 44 and roll <= 53:
            self.government = "Hierarchy"
        elif roll > 53 and roll <= 56:
            self.government = "Magocracy"
        elif roll > 56 and roll <= 58:
            self.government = "Matriarchy"
        elif roll > 58 and roll <= 64:
            self.government = "Militocracy"
        elif roll > 64 and roll <= 74:
            self.government = "Monarchy"
        elif roll > 74 and roll <= 78:
            self.government = "Oligarchy"
        elif roll > 78 and roll <= 80:
            self.government = "Patriarchy"
        elif roll > 80 and roll <= 83:
            self.government = "Meritocracy"
        elif roll > 83 and roll <= 85:
            self.government = "Plutocracy"
        elif roll > 85 and roll <= 92:
            self.government = "Republic"
        elif roll > 92 and roll <= 94:
            self.government = "Satrapy"
        elif roll is 95:
            self.government = "Kleptocracy"
        else:
            self.government = "Theocracy"

    def set_relations(self):
        # Determine racial relations
        roll = random.randint(1, 20)
        if roll <= 10:
            self.relations = "Harmony"
        elif roll > 10 and roll <= 14:
            self.relations = "Tension or rivalry"
        elif roll > 14 and roll <= 16:
            self.relations = "Racial majority are conquerors"
        elif roll is 17:
            self.relations = "Racial minority are rulers"
        elif roll is 18:
            self.relations = "Racial minority are refurgees"
        elif roll is 19:
            self.relations = "Racial majority oppresses minority"
        else:
            self.relations = "Racial minority oppresses majority"

    def set_status(self):
        # Determine ruler's status
        roll = random.randint(1, 20)
        if roll <= 5:
            self.status = "Respected, fair, and just"
        elif roll > 5 and roll <= 8:
            self.status = "Feared tyrant"
        elif roll is 9:
            self.status = "Weakling manipulated by others"
        elif roll is 10:
            self.status = "Illegitimate ruler, simmering civil war"
        elif roll is 11:
            self.status = "Ruled or controlled by a powerful monster"
        elif roll is 12:
            self.status = "Mysterious, anonymous cabal"
        elif roll is 13:
            self.status = "Contested leadership, open fighting"
        elif roll is 14:
            self.status = "Cabal seized power openly"
        elif roll is 15:
            self.status = "Doltish lout"
        elif roll is 16:
            self.status = "On deathbed, claimants compete for power"
        elif roll > 16 and roll <= 18:
            self.status = "Iron-willed but respected"
        else:
            self.status = "Religious leader"

    def set_traits(self):
        # Determine noteable traits
        roll = random.randint(1, 20)
        if roll is 1:
            self.traits = "Canals in place of streets"
        elif roll is 2:
            self.traits = "Massive statue or monument"
        elif roll is 3:
            self.traits = "Grand temple"
        elif roll is 4:
            self.traits = "Large fortress"
        elif roll is 5:
            self.traits = "Verdant parks and orchards"
        elif roll is 6:
            self.traits = "River divides town"
        elif roll is 7:
            self.traits = "Major trade center"
        elif roll is 8:
            self.traits = "Headquarters of a powerful family or guild"
        elif roll is 9:
            self.traits = "Population mostly wealthy"
        elif roll is 10:
            self.traits = "Destitute, rundown"
        elif roll is 11:
            self.traits = "Awful smell (tanneries, open sewers)"
        elif roll is 12:
            self.traits = "Center of trade for one specific good"
        elif roll is 13:
            self.traits = "Site of many battles"
        elif roll is 14:
            self.traits = "Site of a mythic or magical event"
        elif roll is 15:
            self.traits = "Important library or archive"
        elif roll is 16:
            self.traits = "Worship of all gods banned"
        elif roll is 17:
            self.traits = "Sinister reputation"
        elif roll is 18:
            self.traits = "Noteable library or academny"
        elif roll is 19:
            self.traits = "Site of important tomb or graveyard"
        else:
            self.traits = "Built atop ancient ruins"

    def set_knownfor(self):
        # Determine what it is known for...
        roll = random.randint(1, 20)
        if roll is 1:
            self.knownfor = "Delicious cuisine"
        elif roll is 2:
            self.knownfor = "Rude people"
        elif roll is 3:
            self.knownfor = "Greedy merchants"
        elif roll is 4:
            self.knownfor = "Artists and writers"
        elif roll is 5:
            self.knownfor = "Great hero/savior"
        elif roll is 6:
            self.knownfor = "Flowers"
        elif roll is 7:
            self.knownfor = "Hordes of beggars"
        elif roll is 8:
            self.knownfor = "Tough warriors"
        elif roll is 9:
            self.knownfor = "Dark magic"
        elif roll is 10:
            self.knownfor = "Decadence"
        elif roll is 11:
            self.knownfor = "Piety"
        elif roll is 12:
            self.knownfor = "Gambling"
        elif roll is 13:
            self.knownfor = "Godlessness"
        elif roll is 14:
            self.knownfor = "Education"
        elif roll is 15:
            self.knownfor = "Wines"
        elif roll is 16:
            self.knownfor = "High fashion"
        elif roll is 17:
            self.knownfor = "Political intrigue"
        elif roll is 18:
            self.knownfor = "Powerful guilds"
        elif roll is 19:
            self.knownfor = "Strong drink"
        else:
            self.knownfor = "Patriotism"

    def set_calamity(self):
        # Determine current calamity
        roll = random.randint(1, 20)
        if roll is 1:
            self.calamity = "Suspected vampire infestation"
        elif roll is  2:
            self.calamity = "New cults seeking converts"
        elif roll is  3:
            self.calamity = "Important figure died"
        elif roll is  4:
            self.calamity = "War between rival theives' guilds"
        elif roll is  5 or roll is 6:
            self.calamity = "Plague or famine (spark riots)"
        elif roll is  7:
            self.calamity = "Corrupt officials"
        elif roll is  8 or roll is 9:
            self.calamity = "Maurauding monsters"
        elif roll is  10:
            self.calamity = "Powerful wizard has moved into town"
        elif roll is  11:
            self.calamity = "Economic depression (trade disrupted)"
        elif roll is  12:
            self.calamity = "Flooding"
        elif roll is  13:
            self.calamity = "Undead stirring in cemeteries"
        elif roll is  14:
            self.calamity = "Prophecy of doom"
        elif roll is  15:
            self.calamity = "Brink of war"
        elif roll is  16:
            self.calamity = "Internal strife"
        elif roll is  17:
            self.calamity = "Beseiged by enemies"
        elif roll is  18:
            self.calamity = "Scandal threatens powerful families"
        elif roll is  19:
            self.calamity = "Dungeon discovered (adventurers flock to town)"
        else:
            self.calamity = "Religious sects struggle for power"

    def set_buildings(self):
        # Determine number of buildings
        self.buildings = []

        roll = random.randint(1, 100)
        if roll <= 25:
            # Crowded
            numbldgs = floor(self.population*0.05)
        elif roll > 25 and roll <= 75:
            # Standard
            numbldgs = floor(self.population*0.1)
        else:
            # Sparse
            numbldgs = floor(self.population*0.2)

        # Generate building list
        for i in range(numbldgs):
            self.buildings.append(bldg.Building())

    def set_npcs(self):
        # Determine community modifiers
        reroll = 0
        if self.size is "Thorp":
            mod = -3
        elif self.size is "Hamlet":
            mod = -2
        elif self.size is "Village":
            mod = -1
        elif self.size is "Small Town":
            mod = 0
        elif self.size is "Large Town":
            mod = 3
        elif self.size is "Small City":
            mod = 6
            reroll = 1
        elif self.size is "Large City":
            mod = 9
            reroll = 3
        else:
            mod = 12
            reroll = 4

        # Determine highest level NPCs
        adepts = [random.randint(1,6) + mod]
        
        hl_aristocrat = random.randint(1,4) + mod
        hl_barbarian = random.randint(1,4) + mod
        hl_bard = random.randint(1,6) + mod
        hl_cleric = random.randint(1,6) + mod
        hl_commoner = random.randint(4,16) + mod
        if self.size is "Thorp" or self.size is "Hamlet":
            roll = random.randint(1, 100)
            if roll >= 96:
                hl_druid = random.randint(1,6) + mod + 10
            else:
                hl_druid = random.randint(1,6) + mod
        else:
            hl_druid = random.randint(1,6) + mod
        hl_expert = random.randint(3,12) + mod
        hl_fighter = random.randint(1,8) + mod
        hl_monk = random.randint(1,4) + mod
        hl_paladin = random.randint(1,3) + mod
        if self.size is "Thorp" or self.size is "Hamlet":
            roll = random.randint(1, 100)
            if roll >= 96:
                hl_ranger = random.randint(1,3) + mod + 10
            else:
                hl_ranger = random.randint(1,3) + mod
        else:
            hl_ranger = random.randint(1,3) + mod
        hl_rogue = random.randint(1,8) + mod
        hl_sorcerer = random.randint(1,4) + mod
        hl_warrior = random.randint(2,8) + mod
        hl_wizard = random.randint(1,4) + mod

    def buildingwrt(self, fh):
        """
        """
        fileID = open(fh, "w+")
        printblk = "<style>\n  .phb{ background : white;}\n  .phb img{ display : none;}\n  .phb hr+blockquote{background : white;}\n</style>\n\n"
        fileID.write(printblk)
        header = "<div class='wide'>\n##### Building List\n| Number | Building Type | Details |\n|:----:|:---------------:| :----------------------:|\n"
        fileID.write(header)
        start = 0
        final = 44
        pageindex = floor(len(self.buildings)/45)+1
        for j in range(pageindex):
            for i in range((j)*44+start, (j)*44+final):
                if i >= len(self.buildings):
                    break
                strout = "| " + str(i+1) + " | " + self.buildings[i].type + " | " + self.buildings[i].details + " |\n"
                fileID.write(strout)
            if j < (pageindex-1):
                pagediv = "</div>\n\n\\page\n\n<div class='wide'>\n| Number | Building Type | Details |\n|:----:|:---------------:| :----------------------:|\n"
                fileID.write(pagediv)
        footer = "</div>"
        fileID.write(footer)
        fileID.close()
#end of class
