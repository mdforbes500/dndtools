import npc
import unittest

class TestNPC(unittest.TestCase):
    """
    Class for testing NPC class methods.
    """

    def setUp(self):
        """
        Sets up NPC object for testing
        """
        self.npc = npc.NPC("Test NPC")

    #=============ADD TESTS HERE \/\/\/\/===================#
    def test_get_name(self):
        self.assertEqual(self.npc.get_name(), self.npc.name)

    def test_get_rating(self):
        tests = [0, 0.125, 0.25, 0.5, 20]
        for case in tests:
            if self.npc.cr == 0.125:
                self.assertEqual(self.npc.get_rating(), "1/8")
            elif self.npc.cr == 0.25:
                self.assertEqual(self.npc.get_rating(), "1/4")
            elif self.npc.cr == 0.5:
                self.assertEqual(self.npc.get_rating(), "1/2")
            else:
                self.assertEqual(self.npc.get_rating(), str(self.npc.cr))

    def test_get_size(self):
        self.assertEqual(self.npc.get_size(), self.npc.size)

    def test_get_type(self):
        self.assertEqual(self.npc.get_type(), self.npc.type)

    def test_get_race(self):
        self.assertEqual(self.npc.get_race(), self.npc.race)

    def test_get_alignment(self):
        self.assertEqual(self.npc.get_alignment(), self.npc.alignment)

    def test_get_speed(self):
        self.assertEqual(self.npc.get_speed(), self.npc.speed)

    def test_get_ability(self):
        tests = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for index, case in enumerate(tests):
            self.assertEqual(self.npc.get_ability(case), self.npc.abilities[index])
        with self.assertRaises(Exception):
            self.npc.get_ability("fails")

    def test_get_modifier(self):
        tests = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for index, case in enumerate(tests):
            self.assertEqual(self.npc.get_modifier(case), self.npc.modifiers[index])
        with self.assertRaises(Exception):
            self.npc.get_modifier("fails")

    def test_get_proficiency(self):
        self.assertEqual(self.npc.get_proficiency(), self.npc.proficiency)

    def test_get_armor(self):
        self.assertEqual(self.npc.get_armor(), self.npc.armor)

    def test_get_hp(self):
        self.assertEqual(self.npc.get_hp(), self.npc.hp)

    def test_get_skills(self):
        self.assertEqual(self.npc.get_skills(), self.npc.skills)

    def test_get_dicecode(self):
        self.assertEqual(self.npc.get_dicecode(), self.npc.dicecode)

    def test_get_senses(self):
        self.assertEqual(self.npc.get_senses(), self.npc.senses)

    def test_get_languages(self):
        self.assertEqual(self.npc.get_languages(), self.npc.languages)

    def test_get_features(self):
        self.assertEqual(self.npc.get_features(), self.npc.features)

    def test_get_actions(self):
        self.assertEqual(self.npc.get_actions(), self.npc.actions)

    def test_get_inventory(self):
        self.assertEqual(self.npc.get_inventory(), self.npc.inventory)

    def test_get_casterlevel(self):
        self.assertEqual(self.npc.get_casterlevel(), self.npc.cast_level)

    def test_get_if_caster(self):
        self.assertEqual(self.npc.get_if_caster(), self.npc.caster)

    def test_get_cast_ability(self):
        self.assertEqual(self.npc.get_cast_ability(), self.npc.cast_ability)

    def test_get_cast_saving_throw(self):
        self.assertEqual(self.npc.get_cast_saving_throw(), self.npc.cast_save)

    def test_get_spell_attk(self):
        self.assertEqual(self.npc.get_spell_attk(), self.npc.spell_attk)

    def test_get_spell_list(self):
        self.assertEqual(self.npc.get_spell_list(), self.npc.spell_list)

    def test_get_spells(self):
        self.assertEqual(self.npc.get_spells(), self.npc.spells)

    def test_get_slots(self):
        self.assertEqual(self.npc.get_slots(), self.npc.slots)
    #=======================================================#

    def tearDown(self):
        """
        Cleans up after tests are run
        """
        del self.npc

if __name__ == "__main__":
    unittest.main()
