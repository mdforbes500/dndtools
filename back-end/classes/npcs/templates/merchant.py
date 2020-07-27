#!/usr/bin/env python

import random
from math import floor

class Merchant:
    """
    """
    def __init__(self):
        self.traits = None
        self.ideal = None
        self.bond = None
        self.flaw = None

        self.type = None
        self.inventory = []
        self.legendary = False
        self.quality = None
        self.gold = None

        self.set_traits()
        self.set_ideal()
        self.set_bond()
        self.set_flaw()
        self.set_type()
        self.set_quality()

    def set_traits(self):
        self.traits = []

        rolls = random.sample(range(1,8),2)
        for roll in rolls:
            if roll is 1:
                self.traits[roll] = "I greet absolutely everyone with a warm hug."
            elif roll is 2:
                self.traits[roll] = "I have a much better head for numbers than people."
            elif roll is 3:
                self.traits[roll] = "I'm often more willing to barter in favors than coin."
            elif roll is 4:
                self.traits[roll] = "I don't trust adeventurers, not even a little bit."
            elif roll is 5:
                self.traits[roll] = "It's all business with me, no need to be personable."
            elif roll is 6:
                self.traits[roll] = "Repeat customers are my best friends."
            elif roll is 7:
                self.traits[roll] = "I'll haggle all day, until your ears fall off."
            else:
                self.traits[roll] = "I'm convinced my natural showmanship is what earns me customers."
    def set_ideal(self):
        roll = random.randint(1,6)
        if roll is 1:
            self.ideal = "Commerce. Free exchange is the world's greatest equalizer."
        elif roll is 2:
            self.ideal = "Monopoly. Undercutting my rivals and price gouging are the only ways to get ahead."
        elif roll is 3:
            self.ideal = "Salesmanship. I'll sell absolutely anything. My horse, my mother, everthing has a price."
        elif roll is 4:
            self.ideal = "Charity. I try to give discounts or handouts to those that are truly in need."
        elif roll is 5:
            self.ideal = "Finality. No refunds. Ever."
        else:
            self.ideal = "Enjoyment. Buy and selling wars is all a big game to me, one that I love playing."
    def set_bond(self):
        roll = random.randint(1,6)
        if roll is 1:
            self.bond = "I have a sick relative that my business supports."
        elif roll is 2:
            self.bond = "I owe a lot of money to organized crime, and they're threatening to collect. Violently."
        elif roll is 3:
            self.bond = "I'm counting down the days to a peaceful retirement with my spouse or loved ones."
        elif roll is 4:
            self.bond = "I hope to earn enough money to be able to pursue my true love, who is well above my station."
        elif roll is 5:
            self.bond = "I'm on the run from the law, and plan to leave town before they finally recognize me."
        else:
            self.bond = "A large porttion of my money is spent atoning for my shameful past."
    def set_flaw(self):
        roll = random.randint(1,6)
        if roll is 1:
            self.flaw = "Most of my money is spect every night in the tavern."
        elif roll is 2:
            self.flaw = "I have no real faith in the quality of my merchandise, whether or not it is actually good."
        elif roll is 3:
            self.flaw = "If someone undercuts my prices, I'll cut their throat."
        elif roll is 4:
            self.flaw = "I counterfeit currency on the side, and slip it in with the change I give customers."
        elif roll is 5:
            self.flaw = "I never, ever, ever know when to quit, and I refuse to lose a sale."
        else:
            self.flaw = "It's hard for me to respect someone who doesn't know everything about what I'm selling."
    def set_type(self):
        roll = random.randint(1, 100)
        if roll <= 6:
            self.type = 1   # Alcolhol and refreshments
        elif roll > 6 and roll <= 10:
            self.type = 2   # Animals (mounts & pets)
        elif roll > 10 and roll <= 15:
            self.type = 3   # Books and maps (mundane)
        elif roll > 15 and roll <= 19:
            self.type = 4   # Flowers and seeds
        elif roll > 19 and roll <= 25:
            self.type = 5   # Furniture and interior decor
        elif roll > 25 and roll <= 29:
            self.type = 6   # High fashion
        elif roll > 29 and roll <= 34:
            self.type = 7   # Jewlery and gems
        elif roll > 34 and roll <= 38:
            self.type = 8   # Knick-knacks
        elif roll > 38 and roll <= 43:
            self.type = 9   # Leatherworking
        elif roll > 43 and roll <= 48:
            self.type = 10  # Mechanical contraptions
        elif roll > 48 and roll <= 52:
            self.type = 11  # Medium and heavy armor (and shields)
        elif roll > 52 and roll <= 57:
            self.type = 12  # Potions, poisons, and herbs
        elif roll > 57 and roll <= 61:
            self.type = 13  # Religious idols and blessings
        elif roll > 61 and roll <= 66:
            self.type = 14  # Songs and instruments
        elif roll > 66 and roll <= 71:
            self.type = 15  # Spell tomes and scrolls
        elif roll > 71 and roll <= 75:
            self.type = 16  # Theiving supplies
        elif roll > 75 and roll <= 80:
            self.type = 17  # Tools
        elif roll > 80 and roll <= 86:
            self.type = 18  # Vehicles and transportation
        elif roll > 86 and roll <= 91:
            self.type = 19  # Weapons
        elif roll > 91 and roll <= 96:
            self.type = 20  # Weapons
        else:
            self.legendary = True
            roll = random.randint(1, 20)
            if roll <= 2:
                self.type = 21   # Astral travelr
            elif roll > 2 and roll <= 6:
                self.type = 22  # Enchantments
            elif roll is 7:
                self.type = 23  # Fey bargins
            elif roll > 7 and roll <= 11:
                self.type = 24  # Megic items
            elif roll > 11 and roll <= 14:
                self.type = 25  # Magical creatures
            elif roll > 14 and roll <= 18:
                self.type = 26  # Necromancy
            elif roll is 19:
                self.type = 27  # Needful things
            else:
                self.type = 28  # Time-lost
    def set_quality(self):
        roll = random.randint(1,20)
        if roll <= 2:
            self.quality = 0    # Atrocious
            self.gold = random.randint(1,10) * 20
        elif roll > 2 and roll <= 6:
            self.quality = 1    # Poor
            self.gold = random.randint(1,10) * 50
        elif roll > 6 and roll <= 12:
            self.quality = 2    # Medium
            self.gold = random.randint(1,10) * 100
        elif roll > 12 and roll <= 17:
            self.quality = 3    # Good
            self.gold = random.randint(1,10) * 250
        else:
            self.quality = 4    # Excellent
            self.gold = random.randint(1,10) * 500

        if self.legendary is True and self.quality < 2:
            self.set_quality()
    def set_inventory(self):
        if self.type is 1:
            if self.quality is 0:
                self.inventory.append(["Ale, inferior", "2cp/mug", random.randint(1,4)*100, None, "Flavor will"])
