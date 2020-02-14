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
    #=======================================================#

    def tearDown(self):
        """
        Cleans up after tests are run
        """
        del npc

if __name__ == "__main__":
    unittest.main()
