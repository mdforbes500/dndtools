#!/usr/bin/python

class Item:

    def __init__(self, name, type, cost, weight):
        self.name = name
        self.type = type
        self.cost = cost
        self.weight = weight

    def __eq__(self, object):
        if self.name == object.name:
            if self.type == object.type:
                if self.cost == object.cost:
                    if self.weight == object.weight:
                        return True
        return False

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_cost(self):
        return self.cost

    def get_weight(self):
        return self.weight

    def set_name(self, name):
        self.name = name

    def set_type(self, type):
        self.type = type

    def set_cost(self, cost):
        self.cost = cost

    def set_weight(self, weight):
        self.weight = weight
