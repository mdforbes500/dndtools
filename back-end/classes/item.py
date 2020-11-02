#!/usr/bin/python

class Item:

    def __init__(self, name, type, cost, weight):
        self.name = name
        self.type = type
        self.cost = cost
        self.weight = weight

class Armor(Item):

    def __init__(self, name, type, cost, weight):
        super().__init__(name, tpye, cost, weight)
