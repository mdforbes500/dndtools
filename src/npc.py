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
        self.speed = 30
        self.abilities = [10,10,10,10,10,10]
        self.modifiers = [0,0,0,0,0,0]
        self.proficiency = 2
        self.armor = "            <li><strong>Armor Class</strong> 10</li>\n"
        self.hp = "            <li><strong>Hit Points</strong> 1 (1d6)</li>\n"
        self.skills = {}
        self.senses = []
        self.languages = []
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
        armor = 0
        for item in self.items:
            if item.type == "armor" and item.isequipped == True:
                if item.subtype == "Medium":
                    armor = item.ac + self.get_modifier("DEX")
                elif item.subtype == "Heavy":
                    armor = item.ac
                elif item.subtype == "Shield":
                    armor = armor + item.ac
                else:
                    armor = item.ac
            else:
                print("Item is not armor.")
        self.armor = "            <li><strong>Armor Class</strong> {0}</li>\n".format(armor)

    def update_dicecode(self):
        cr = self.cr
        if cr == 0:
            upper = 6
            lower = 1
        elif cr == 0.125:
            upper = 35
            lower = 7
        elif cr == 0.25:
            upper = 49
            lower = 36
        elif cr == 0.5:
            upper = 70
            lower = 50
        elif cr == 1:
            upper = 85
            lower = 71
        elif cr == 2:
            upper = 100
            lower = 86
        elif cr == 3:
            upper = 115
            lower = 101
        elif cr == 4:
            upper = 130
            lower = 116
        elif cr == 5:
            upper = 145
            lower = 131
        elif cr == 6:
            upper = 160
            lower = 146
        elif cr == 7:
            upper = 175
            lower = 161
        elif cr == 8:
            upper = 190
            lower = 176
        elif cr == 9:
            upper = 205
            lower = 191
        elif cr == 10:
            upper = 220
            lower = 206
        elif cr == 11:
            upper = 235
            lower = 221
        elif cr == 12:
            upper = 250
            lower = 236
        elif cr == 13:
            upper = 265
            lower = 251
        elif cr == 14:
            upper = 280
            lower = 226
        elif cr == 15:
            upper = 295
            lower = 281
        elif cr == 16:
            upper = 310
            lower = 296
        elif cr == 17:
            upper = 325
            lower = 311
        elif cr == 18:
            upper = 340
            lower = 326
        elif cr == 19:
            upper = 355
            lower = 341
        elif cr == 20:
            upper = 400
            lower = 356
        elif cr == 21:
            upper = 445
            lower = 401
        elif cr == 22:
            upper = 490
            lower = 446
        elif cr == 23:
            upper = 535
            lower = 491
        elif cr == 24:
            upper = 580
            lower = 536
        elif cr == 25:
            upper = 625
            lower = 581
        elif cr == 26:
            upper = 670
            lower = 626
        elif cr == 27:
            upper = 715
            lower = 671
        elif cr == 28:
            upper = 760
            lower = 716
        elif cr == 29:
            upper = 805
            lower = 761
        elif cr == 30:
            upper = 850
            lower = 806
        else:
            print("Not a valid CR range.")
            return None

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
            return None

        #starting values
        num_dice = 1
        temp_hp = num_dice*(sizemod + self.modifiers[2])
        while True:
            temp_hp = num_dice*(sizemod + self.modifiers[2])
            if temp_hp <= upper and temp_hp >= lower:
                break
            num_dice = num_dice + 1

        dice_code = "({0}d{1}+{2})".format(num_dice, sizemod, self.get_modifier("CON"))
        hit_points = int(num_dice*avg_hp + self.modifiers[2])
        self.hp = "            <li><strong>Hit Points</strong> {0} {1}</li>\n".format(hit_points, dice_code)

    #Print method
    def __str__(self):
        header = "\
<head>\n\
   <link rel=\"stylesheet\" href=\"CSS/phb.css\" />\n\
   <style>\n\
      .phb{ background : white;}\n\
      .phb img{ display : none;}\n\
      .phb hr+blockquote{background : white;}\n\
   </style>\n\
</head>\n\n"
        body="\
<body>\n\
   <div class = 'phb'>\n\
      <hr>\n\
      <blockquote>\n\
         <h2 id=\"{0}\">{0}</h2>\n\
         <p><em>{1} {2}{3}, {4}</em></p>\n\
         <hr>\n\
         <ul>\n".format(self.name, self.size, self.type, self.race, self.alignment)
        armor = self.armor
        hit_points = self.hp
        speed = "            <li><strong>Speed</strong> {0} ft.</li>\n         </ul>\n".format(self.speed)
        abilities="\
         <hr>\n\
         <table>\n\
            <thead>\n\
               <tr>\n\
                  <th style=\"text-align:center\">STR</th>\n\
                  <th style=\"text-align:center\">DEX</th>\n\
                  <th style=\"text-align:center\">CON</th>\n\
                  <th style=\"text-align:center\">INT</th>\n\
                  <th style=\"text-align:center\">WIS</th>\n\
                  <th style=\"text-align:center\">CHA</th>\n\
                </tr>\n\
            </thead>\n\
            <tbody>\n\
               <tr>\n\
                  <td style=\"text-align:center\">{0} ({1})</td>\n\
                  <td style=\"text-align:center\">{2} ({3})</td>\n\
                  <td style=\"text-align:center\">{4} ({5})</td>\n\
                  <td style=\"text-align:center\">{6} ({7})</td>\n\
                  <td style=\"text-align:center\">{8} ({9})</td>\n\
                  <td style=\"text-align:center\">{10} ({11})</td>\n\
               </tr>\n\
            </tbody>\n\
            </table>\n".format(self.abilities[0], self.modifiers[0], self.abilities[1], self.modifiers[1], self.abilities[2], self.modifiers[2], self.abilities[3], self.modifiers[3], self.abilities[4], self.modifiers[4], self.abilities[5], self.modifiers[5])
        skills ="\
            <hr>\n\
            <ul>\n\
               <li><strong>Skills</strong> Medicine +4, Religion +2</li>\n\
               <li><strong>Senses</strong> passive Perception 10</li>\n\
               <li><strong>Languages</strong> any one language (usually Common)</li>\n\
               <li><strong>Challenge</strong> 1/4 (50 XP)</li>\n\
            </ul>\n\
            <hr>\n"
        spells ="\
            <p><strong><em>Spellcasting</em></strong>. The acolyte is a 1st-level spellcaster. Its spellcasting ability it Wisdom (spell save DC 12, +4 to hit with spell attacks). The acolyte has the following cleric spells prepared:</p>\n\
            <p>Cantrips (at will): <em>light, sacred flame, thaumaturgy</em></p>\n\
            <p>1st level (3 slots): <em>bless, cure wounds, sanctuary</em></p>\n"
        actions ="\
            <h3 id=\"actions\">Actions</h3>\n\
            <p><strong><em>Club.</em></strong> <em>Melee Weapon Attack:</em> +2 to hit, reach 5ft., one target. <em>Hit</em> 2 (1d4) bludgeoning damage.</p>\n\
      </blockquote>\n\
      <div class='pageNumber auto'></div>\n\
   </div>\n\
</body>"
        block = header + body + self.armor + hit_points + speed + abilities
        return block
