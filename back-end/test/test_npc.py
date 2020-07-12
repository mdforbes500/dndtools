#!/usr/bin/python3

from context import classes
import unittest
import os

class TestNPC(unittest.TestCase):
    """
    Class for testing NPC class methods.
    """

    def setUp(self):
        """
        Sets up NPC object for testing
        """
        self.npc = classes.npcs.npc.NPC("Test")

    #====================ADD TESTS HERE=====================#
    def test_npc(self):
        self.assertEqual(self.npc.name, "Test")
        self.assertEqual(self.npc.cr, 0)
        self.assertEqual(self.npc.size, None)
        self.assertEqual(self.npc.type, None)
        self.assertEqual(self.npc.race, None)
        self.assertEqual(self.npc.alignment, None)
        self.assertEqual(self.npc.speed, {"ground": None, "fly": None, "swim": None, "climb": None})
        self.assertEqual(self.npc.abilities, [None,None,None,None,None,None])
        self.assertEqual(self.npc.modifiers, [None,None,None,None,None,None])
        self.assertEqual(self.npc.proficiency, 0)
        self.assertEqual(self.npc.armor, 0)
        self.assertEqual(self.npc.hp, 0)
        self.assertEqual(self.npc.dicecode, None)
        self.assertEqual(self.npc.skills, None)
        self.assertEqual(self.npc.senses, None)
        self.assertEqual(self.npc.languages, None)
        self.assertEqual(self.npc.features, None)
        self.assertEqual(self.npc.actions, None)
        self.assertEqual(self.npc.inventory, None)
        self.assertEqual(self.npc.cast_level, 0)
        self.assertEqual(self.npc.caster, None)
        self.assertEqual(self.npc.cast_ability, None)
        self.assertEqual(self.npc.cast_save, None)
        self.assertEqual(self.npc.spell_attk, None)
        self.assertEqual(self.npc.spell_list, None)
        self.assertEqual(self.npc.spells, None)
        self.assertEqual(self.npc.slots, None)

    def test_export(self):
        self.npc.export_json("test.json")
        self.assertEqual(os.path.exists("test.json"), True)

    def test_import(self):
        self.npc.import_json("test.json")
    #=======================================================#

    def tearDown(self):
        """
        Cleans up after tests are run
        """
        # if os.path.exists("test.json"):
        #     os.remove("test.json")
        del self.npc

if __name__ == "__main__":
    unittest.main()
