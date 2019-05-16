#!/usr/bin/python

import item

class Armor(item.Item):

    def __init__(self, name, subtype, cost, ac, str, stealth, weight):
        super().__init__(self, name, "armor", cost, weight)
        self.ac = ac
        self.subtype = subtype
        self.str = str
        self.stealth = stealth
        self.isequipped = False
