#!/usr/bin/python

from context import classes as cs
import unittest

class TestNPC(unittest.TestCase):
    """
    Class for testing NPC class methods.
    """

    def setUp(self):
        """
        Sets up NPC object for testing
        """
        self.npc = cs.npc.NPC("Test NPC")

    #=============ADD TESTS HERE \/\/\/\/===================#
    def test_aarakocra(self):
        aarakocra = cs.races.aarakocra(self.npc)
        self.assertEqual(self.npc.name, "Test NPC")
        self.assertEqual(self.npc.cr, 0)
        self.assertEqual(self.npc.size, "Medium")
        self.assertEqual(self.npc.type, "humanoid")
        self.assertEqual(self.npc.race, "(aarakocra)")
        self.assertEqual(self.npc.alignment, "neutral")
        self.assertEqual(self.npc.speed, {"ground": 20, "fly": 50, "swim": 0, "climb": 0})
        self.assertEqual(self.npc.abilities, [10,12,10,10,12,10])
        self.assertEqual(self.npc.modifiers, [0,1,0,0,1,0])
        self.assertEqual(self.npc.proficiency, 2)
        self.assertEqual(self.npc.armor, 10)
        self.assertEqual(self.npc.hp, 4)
        self.assertEqual(self.npc.dicecode, "1d8")
        self.assertEqual(self.npc.skills, {})
        self.assertEqual(self.npc.senses, {"passive Perception": 11})
        self.assertEqual(self.npc.languages, ["Common", "Auran"])
        self.assertEqual(self.npc.features, {"Dive Attack": "If the aarakocra is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 3 (1d6) damage to the target"})
        self.assertEqual(self.npc.actions, {
            "Talon": ['Melee', 2, 5, 2, '1d4 + 0', 'piercing'],
            "Club": ['Melee', 2, 5, 2, '1d4 + 0', 'bludgeoning']
        })
        self.assertEqual(self.npc.inventory, {})
        self.assertEqual(self.npc.cast_level, 0)
        self.assertEqual(self.npc.caster, False)
        self.assertEqual(self.npc.cast_ability, "")
        self.assertEqual(self.npc.cast_save, 0)
        self.assertEqual(self.npc.spell_attk, 0)
        self.assertEqual(self.npc.spell_list, "")
        self.assertEqual(self.npc.spells, [])
        self.assertEqual(self.npc.slots, [])
    #=======================================================#

    def tearDown(self):
        """
        Cleans up after tests are run
        """
        del self.npc

if __name__ == "__main__":
    unittest.main()
