#!/usr/bin/python3

from context.classes.npcs import acolyte
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
        self.npc = acolyte.Acolyte()

    #====================ADD TESTS HERE=====================#
    def test_acolyte(self):
        self.assertEqual(self.npc.name, "Acolyte")
        self.assertEqual(self.npc.cr, 0.25)
        self.assertEqual(self.npc.size, "Medium")
        self.assertEqual(self.npc.type, "humanoid")
        self.assertEqual(self.npc.race, "human")
        self.assertEqual(self.npc.alignment, "neutral")
        self.assertEqual(self.npc.speed, {"ground": 30, "fly": None, "swim": None, "climb": 15})
        self.assertEqual(self.npc.abilities, [10,10,10,10,14,11])
        self.assertEqual(self.npc.modifiers, [0,0,0,0,2,0])
        self.assertEqual(self.npc.proficiency, 2)
        self.assertEqual(self.npc.armor, 10)
        self.assertGreaterEqual(self.npc.hp, 2)
        self.assertLessEqual(self.npc.hp, 16)
        self.assertEqual(self.npc.dicecode, "2d8")
        self.assertEqual(self.npc.skills, {"Medicine": 4, "Religion": 2})
        self.assertEqual(self.npc.senses, {"passive Perception": 12})
        self.assertEqual(self.npc.languages, ["Common"])
        self.assertEqual(self.npc.features, {
            "Spellcasting": {
                "caster level": 1,
                "caster ability": "Wisdom",
                "spell save": 12,
                "spell attack": 4,
                "spell list": "cleric",
                "spellbook": {
                    "0": ["light", "sacred flame", "thaumaturgy"],
                    "1": ["bless", "cure wounds", "sanctuary"]
                },
                "spell slots": {
                    "0": 0,
                    "1": 3
                }
            }
        })
        self.assertEqual(self.npc.actions, None)
        self.assertEqual(self.npc.inventory, None)

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
