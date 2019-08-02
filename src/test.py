#!/usr/bin/env python

import settlement as set

test = set.Settlement("Test")
print(test.name)
print(test.size)
print(test.population)
print(test.gplimit)
print(test.wealth)
print(test.powerctrs)
print(test.government)
print(test.relations)
print(test.status)
print(test.traits)
print(test.knownfor)
print(test.calamity)
for i in range(len(test.buildings)):
    print(test.buildings[i])
print(test.npcs)
print(len(test.buildings))
test.buildingwrt("test.txt")
