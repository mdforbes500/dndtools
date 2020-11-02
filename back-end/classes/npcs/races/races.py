#!/usr/bin/python3
import classes.npc as npc

class Race:

    def __init__(self) -> None:
        """
        Base constructor for D&D Races
        """
        self.size = ""
        self.type = ""
        self.race = ""
        self.alignment_center = ""
        self.features = {}
        self.actions = {}
        self.speed = {}
        self.languages = []

    def update_template(self, template: npc.NPC):
        """
        Updates NPC template with racial characteristics
        """
        pass

class Aarakocra(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(aarakocra)"
        self.alignment_center = "neutral good"
        self.dex_abil_mod = 2 # +2 to Dex
        self.wis_abil_mod = 2 # +2 to Wis
        self.features["Dive Attack"] = "If the aarakocra is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 3 (1d6) damage to the target"
        self.actions["Talon"] = "Melee Weapon Attack: {attk_mod} to hit, reach 5 ft., one target. Hit: {avg_dmg} ( 1d4 + {dicecode}) slashing damage.".format(
            attk_mod = template.modifiers[0], 
            avg_dmg = template.find_damage(4, template.modifiers[0]), 
            dicecode = template.modifiers[0]
        )
        self.speed["ground"] = 20
        self.speed["fly"] = 50
        self.languages.append("Auran")

class Bullywug(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(bullywug)"
        self.alignment_center = "neutral evil"
        self.int_abil_mod = -2 # -2 to Int
        self.cha_abil_mod = -2 # -2 to Cha
        self.features["Amphibious"] = "The bullywug can breathe air and water."
        self.features["Speak with Frogs and Toads"] = "The bullywug can communicate simple concepts to frogs and toads when it speaks in Bullywug."
        self.features["Swamp Camouflage"] = "The bullywug has advantage on Dexterity (Stealth) checks made to hide in swampy terrain."
        self.features["Standing Leap"] = "The bullywug's long jump is up to 20 feet and its high jump is up to 10 feet, with or without a running start."
        self.speed["ground"] = 20
        self.speed["swim"] = 40
        self.languages.append("Bullywug")