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
        self.assertEqual(self.npc.race, "(aarakocra)")
        self.assertEqual(self.npc.abilities, [10,12,10,10,12,10])

    #=======================================================#

    def tearDown(self):
        """
        Cleans up after tests are run
        """
        del self.npc

if __name__ == "__main__":
    unittest.main()
