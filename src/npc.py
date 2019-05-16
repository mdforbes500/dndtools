#!/usr/bin/python

import item
import armor
import random
import math

class NPC:
    """
    NPC: Contains methods for modifying basic stat block to create a new
    non-player character.
    """
    def __init__(self, name):
        self.name = str(name)
        self.cr = 0
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(human)"
        self.alignment = "neutral"
        self.abilities = [10,10,10,10,10,10]
        self.modifiers = [0,0,0,0,0,0]
        self.proficiency = 2
        self.armor = 10
        self.hp = 1
        self.dicecode = "(1d6)"
        self.features = {}
        self.actions = {}
        self.items = {}
        self.spells = []

    #Accessor methods
    def get_name(self):
        return str(self.name)

    def get_rating(self):
        if self.cr == 0.125:
            return "1/8"
        elif self.cr == 0.25:
            return "1/4"
        elif self.cr == 0.5:
            return "1/2"
        else:
            return "{0:.0f}".format(self.cr)

    def get_size(self):
        return str(self.size)

    def get_type(self):
        return str(self.type)

    def get_race(self):
        return str(self.race)

    def get_alignment(self):
        return str(self.alignment)

    def get_ability_score(self, ability):
        ability = str(ability)
        if ability == "STR":
            score = self.abilities[0]
        elif ability == "DEX":
            score = self.abilities[1]
        elif ability == "CON":
            score = self.abilities[2]
        elif ability == "INT":
            score = self.abilities[3]
        elif ability == "WIS":
            score = self.abilities[4]
        elif ability == "CHA":
            score = self.abilities[5]
        else:
            print("INPUT ERROR: Not a recognized ability tag!")
            return None
        return str(score)

    def get_modifier(self, ability):
        ability = str(ability)
        if ability == "STR":
            modifier = self.modifiers[0]
        elif ability == "DEX":
            modifier = self.modifiers[1]
        elif ability == "CON":
            modifier = self.modifiers[2]
        elif ability == "INT":
            modifier = self.modifiers[3]
        elif ability == "WIS":
            modifier = self.modifiers[4]
        elif ability == "CHA":
            modifier = self.modifiers[5]
        else:
            print("INPUT ERROR: Not a recognized ability tag!")
            return None
        return str(modifier)

    def get_proficiency(self):
        output = "+{0}".format(self.proficiency)
        return output

    def get_armor(self):
        return self.armor

    def get_hp(self):
        return self.hp

    def get_dicecode(self):
        return self.dicecode

    def get_feature(self, feature):
        feature = str(feature)
        return self.features[feature]

    def get_action(self, action):
        action = str(action)
        return self.actions[action]

    def get_item(self, item):
        item = str(item)
        return self.items[item]

    #Mutator methods
    def set_name(self, name):
        self.name = str(name)

    def set_size(self, size):
        size = str(size)
        #FIXME: There has got to be a better way to check these.
        if size == "Tiny":
            self.size = size
        elif size == "Small":
            self.size = size
        elif size == "Medium":
            self.size = size
        elif size == "Large":
            self.size = size
        elif self.size == "Huge":
            self.size = size
        elif self.size == "Gargantuan":
            self.size == size
        else:
            print("INPUT ERROR: Please choose an appropriate size!")

    def set_type(self, type):
        type = str(type)
        if type == "aberration":
            self.type = type
        elif type == "beast":
            self.type = type
        elif type == "celestial":
            self.type = type
        elif type == "construct":
            self.type = type
        elif type == "dragon":
            self.type = type
        elif type == "elemental":
            self.type = type
        elif type == "fey":
            self.type = type
        elif type == "fiend":
            self.type = type
        elif type == "giant":
            self.type = type
        elif type == "humanoid":
            self.type = type
        elif type == "monstrosity":
            self.type = type
        elif type =="ooze":
            self.type = type
        elif type == "plant":
            self.type = type
        elif type == "undead":
            self.type = type
        else:
            print("INPUT ERROR: Please choose an appropriate type!")
            print("(N.B.: Make sure it is lowercase.)")

    def set_alignment(self, alignment):
        alignment = str(alignment)
        if alignment == "lawful good":
            self.alignment = alignment
        elif alignment == "neutral good":
            self.alignment = alignment
        elif alignment == "chaotic good":
            self.alignment = alignment
        elif alignment == "lawful neutral":
            self.alignment = alignment
        elif alignment == "neutral":
            self.alignment = alignment
        elif alignment == "chaotic neutral":
            self.alignment = alignment
        elif alignment == "lawful evil":
            self.alignment = alignment
        elif alignment == "neutral evil":
            self.alignment = alignment
        elif alignment == "chaotic evil":
            self.alignment = alignment
        elif alignment == "unaligned":
            self.alignment = alignment
        else:
            print("INPUT ERROR: Please choose a valid alignment!")
            print("(N.B.: Make sure it is lowercase.)")

    def set_ability_score(self, ability, score):
        ability = str(ability)
        score = int(score)
        if score <= 30 and score > 0:
            if ability == "STR":
                self.abilities[0] = score
            elif ability == "DEX":
                self.abilities[1] = score
            elif ability == "CON":
                self.abilities[2] = score
            elif ability == "INT":
                self.abilities[3] = score
            elif ability == "WIS":
                self.abilities[4] = score
            elif ability == "CHA":
                self.abilities[5] = score
            else:
                print("INPUT ERROR: Not a recognized ability tag!")
        else:
            print("INPUT ERROR: Invalid score range!")
            print("Please choose a value between 1 and 30.")

    def update_modifiers(self):
        for index, modifer in enumerate(self.modifiers):
            modifer = (self.abilities[index] - 10)//2
            self.modifiers[index] = modifier

    def set_challenge_rating(self, cr):
        cr = float(cr)
        if cr >= 0:
            self.cr = cr
        else:
            print("INPUT ERROR: Please select a valid CR!")
            return None

        if cr >= 0 and cr <= 4:
            self.proficiency = 2
        elif cr > 4 and cr <= 8:
            self.proficiency = 3
        elif cr > 8 and cr <= 12:
            self.proficiency = 4
        elif cr > 12 and cr <= 16:
            self.proficiency = 5
        elif cr > 16 and cr <= 20:
            self.proficiency = 6
        elif cr > 20 and cr <= 24:
            self.proficiency = 7
        elif cr > 24 and cr <= 28:
            self.proficiency = 8
        else:
            self.proficiency = 9

    def add_item(self, item):
        self.items[item.get_name()] = item

    def equip(self, item):
        if item.type == "armor" and item.isequipped == False:
            if self.get_ability_score("STR") >= item.str:
                item.isequipped = True
        elif item.type !="armor" and item.isequipped == False:
            item.isequipped = True

    def unequip(self, item):
        if item.isequipped == True:
            item.isequipped = False

    def update_armor(self):
        for item in self.items:
            if item.type == "armor" and item.isequipped == True:
                if item.subtype == "Medium":
                    self.ac = item.ac + self.get_modifier("DEX")
                elif item.subtype == "Heavy":
                    self.ac = item.ac
                elif item.subtype == "Shield":
                    self.ac = self.ac + item.ac
                else:
                    self.ac = item.ac
            else:
                print("Item is not armor.")

    def set_hp(self):
        """
        SET_HP: Sets the HP at a random number based upon challenge rating.
        """
        cr = self.cr
        if cr == 0:
            self.hp = random.randint(1,6)
        elif cr == 0.125:
            self.hp = random.randint(7,35)
        elif cr == 0.25:
            self.hp = random.randint(36,49)
        elif cr == 0.5:
            self.hp = random.randint(50,70)
        elif cr == 1:
            self.hp = random.randint(71,85)
        elif cr == 2:
            self.hp = random.randint(86,100)
        elif cr == 3:
            self.hp = random.randint(101,115)
        elif cr == 4:
            self.hp = random.randint(116,130)
        elif cr == 5:
            self.hp = random.randint(131,145)
        elif cr == 6:
            self.hp = random.randint(146,160)
        elif cr == 7:
            self.hp = random.randint(161,175)
        elif cr == 8:
            self.hp = random.randint(176,190)
        elif cr == 9:
            self.hp = random.randint(191,205)
        elif cr == 10:
            self.hp = random.randint(206,220)
        elif cr == 11:
            self.hp = random.randint(221,235)
        elif cr == 12:
            self.hp = random.randint(236,250)
        elif cr == 13:
            self.hp = random.randint(251,265)
        elif cr == 14:
            self.hp = random.randint(266,280)
        elif cr == 15:
            self.hp = random.randint(281,295)
        elif cr == 16:
            self.hp = random.randint(296,310)
        elif cr == 17:
            self.hp = random.randint(311,325)
        elif cr == 18:
            self.hp = random.randint(326,340)
        elif cr == 19:
            self.hp = random.randint(341,355)
        elif cr == 20:
            self.hp = random.randint(356,400)
        elif cr == 21:
            self.hp = random.randint(401,445)
        elif cr == 22:
            self.hp = random.randint(446,490)
        elif cr == 23:
            self.hp = random.randint(491,535)
        elif cr == 24:
            self.hp = random.randint(536,580)
        elif cr == 25:
            self.hp = random.randint(581,625)
        elif cr == 26:
            self.hp = random.randint(626,670)
        elif cr == 27:
            self.hp = random.randint(671,715)
        elif cr == 28:
            self.hp = random.randint(716,760)
        elif cr == 29:
            self.hp = random.randint(761,805)
        elif cr == 30:
            self.hp = random.randint(806,850)
        else:
            print("Not a valid CR range.")

    def update_dicecode(self):
        self.set_hp()
        size = self.get_size()
        if size == "Tiny":
            sizemod = 4
            avg_hp = 2.5
        elif size == "Small":
            sizemod = 6
            avg_hp = 3.5
        elif size == "Medium":
            sizemod = 8
            avg_hp = 4.5
        elif size == "Large":
            sizemod = 10
            avg_hp = 5.5
        elif size == "Huge":
            sizemod = 12
            avg_hp = 6.5
        elif size == "Gargantuan":
            sizemod = 20
            avg_hp = 10.5
        else:
            print("Not a valid size.")

        max_dice = math.ceil(float(self.hp)/float(sizemod + self.modifiers[2]))
        min_dice = self.hp//(1 + self.modifiers[2])
        #bounds
        max_hp = max_dice*(sizemod + self.modifiers[2])
        min_hp = min_dice*(sizemod + self.modifiers[2])
        #starting values
        num_dice = 1
        temp_hp = num_dice*(sizemod + self.modifiers[2])
        while True:
            if temp_hp <= max_hp and temp_hp >= min_hp:
                 num_dice = num_dice + 1
                 temp_hp = num_dice*(sizemod + self.modifiers[2])
                 if temp_hp <= self.hp + 6 + self.modifiers[2] and temp_hp >= self.hp - 1 - self.modifiers[2]:
                     break
        dice_code = "({0}d{1}+{2})".format(num_dice, sizemod, self.get_modifier("CON"))
        self.dicecode = dice_code
