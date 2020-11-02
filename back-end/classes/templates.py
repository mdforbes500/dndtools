#!/usr/bin/python

import random as rd
from . import npc

class Acolyte(npc.NPC):

    def __init__(self):
        super().__init__("Acolyte")
        self.cr = 0.25
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(human)"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 0}
        self.abilities = [10, 10, 10, 10, 14, 11]
        self.update_modifiers()
        self.proficiency = 2
        self.armor = 10
        self.hp = 9
        self.dicecode = "2d8"
        self.skills = {"Medicine":4, "Religion":2}
        self.senses = {"passive Perception": 12}
        self.languages = ["Common"]
        self.cast_level = "1st"
        self.caster = True
        self.cast_ability = "Wisdom"
        self.cast_save = 12
        self.spell_attk = 4
        self.spell_list = "cleric"
        self.spells = [["light", "sacred flame", "thaumaturgy"],["bless", "cure wounds", "sanctuary"]]
        self.slots = [0, 3]
        self.features = {"Spellcasting" : ""}
        self.actions = {
            "Club": "<i>Melee Weapon Attack</i>: +{} to hit, reach 5 ft., one target. <i>Hit</i>: {} (1d4 + {}) bludgeoning damage.".format(self.find_attk_mod(self.modifiers[0]), self.find_damage(4, self.modifiers[0]), self.modifiers[0])
        }
        self.inventory = {}
        self.vulnerable = []
        self.dmg_resist = []
        self.cond_resist = []
        self.dmg_immune = []
        self.cond_immune = []

class Archmage(npc.NPC):

    def __init__(self):
        super().__init__("Archmage")
        self.cr = 12
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(human)"
        self.alignment = "neutral"
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 0}
        self.abilities = [10, 14, 12, 20, 15, 16]
        self.update_modifiers()
        self.proficiency = 4
        self.armor = 12
        self.hp = 99
        self.dicecode = "18d8 + 18"
        self.saves = {"Int":9, "Wis":6}
        self.skills = {"Arcana":13, "History":13}
        self.senses = {"passive Perception": 12}
        self.languages = ["Common"] #add 5 more
        self.cast_level = "18th"
        self.caster = True
        self.cast_ability = "Intelligence"
        self.cast_save = 17
        self.spell_attk = 9
        self.spell_list = "wizard"
        self.spells = [
            ["fire bolt", "light", "mage hand", "prestidigitation", "shocking grasp"],
            ["detect magic", "identify", "mage armor", "magic missile"],
            ["detect thoughts", "mirror image", "misty step"],
            ["counterspell", "fly", "lightning bolt"],
            ["banishment", "fire shield", "stoneskin"],
            ["cone of cold", "scrying", "wall of force"],
            ["globe of invulnerability"],
            ["teleport"],
            ["mind blank"],
            ["time stop"]
        ]
        self.slots = [0, 4, 3, 3, 3, 3 ,1 ,1 ,1 ,1]
        self.features = {
            "Magic Resistance": "The archmage has advantage on saving throws against spells and othe magical effects." ,
            "Spellcasting" : ""
        }
        self.actions = {
            "Dagger": [
                'Melee or Ranged',
                self.find_attk_mod(self.modifiers[1]),
                5,
                self.find_damage(4, self.modifiers[1]),
                '1d4 + {}'.format(self.modifiers[1]),
                'piercing'
            ],
        }
        self.inventory = {}
        self.vulnerable = []
        self.dmg_resist = ["damage from spells", "nonmagical bludgeoning, piercing, and slashing"]
        self.cond_resist = []
        self.dmg_immune = []
        self.cond_immune = []

class Assassin(npc.NPC):

    def __init__(self):
        super().__init__("Assassin")
        self.cr = 8
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(human)"
        self.alignment = "neutral" #non-good
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 0}
        self.abilities = [11, 16, 14, 13, 11, 10]
        self.update_modifiers()
        self.proficiency = 3
        self.hp = 78
        self.dicecode = "12d8 + 24"
        self.saves = {"Dex": 6, "Int": 4}
        self.skills = {"Acrobatics": 6, "Deception": 3, "Perception": 3, "Stealth": 9}
        self.senses = {"passive Perception": 13}
        self.languages = ["Thieves' cant"] #add 2 more
        self.cast_level = None
        self.caster = False
        self.cast_ability = None
        self.cast_save = None
        self.spell_attk = None
        self.spell_list = None
        self.spells = None
        self.slots = None
        self.features = {
            "Assassinate": "During its first turn, the assassin has advantage on attack rolls against any creature that hasn't taken a turn. Any hit the assassin scores against a surprised creature is a critcal hit.",
            "Evasion": "If the assassin is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, the assassin instead takes no damage if it succeeds on the saving throw, and only half damage if it fails.",
            "Sneak Attack": "Once per turn, the assassin deals an extra 14 (4d6) damage when it hits a target with a weapon attack and has advantage on the attack roll, or when the target is within 5 feet of an ally of the assassin that isn't incapacitated and the assassin doesn't have disadvantage on the attack roll."
        }
        self.actions = {
            "Multiattack": "The assassin makes two shortsword attacks.",
            "Shortsword": [
                'Melee',
                self.find_attk_mod(self.modifiers[1]),
                5,
                self.find_damage(4, self.modifiers[1]),
                '1d4 + {}'.format(self.modifiers[1]),
                'piercing'
            ],
        }
        self.inventory = {}
        self.vulnerable = []
        self.dmg_resist = ["damage from spells", "nonmagical bludgeoning, piercing, and slashing"]
        self.cond_resist = []
        self.dmg_immune = []
        self.cond_immune = []

class Bandit(npc.NPC):

    def __init__(self):
        super().__init__("Bandit")
        self.cr = 0.125
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(human)"
        self.alignment = "neutral" #any non-lawful
        self.speed = {"ground": 30, "fly": 0, "swim": 0, "climb": 0}
        self.abilities = [11, 12, 12, 10, 10, 10]
        self.update_modifiers()
        self.proficiency = 2
        self.armor = 12
        self.hp = 11
        self.dicecode = "2d8+2"
        self.skills = {}
        self.senses = {"passive Perception": 10}
        self.languages = ["Common"]
        self.cast_level = "1st"
        self.caster = False
        self.cast_ability = None
        self.cast_save = None
        self.spell_attk = None
        self.spell_list = None
        self.spells = None
        self.slots = None
        self.features = {}
        self.actions = {
            "Scimitar": "<i>Melee Weapon Attack</i>: +{} to hit, reach 5 ft., one target. <i>Hit</i>: {} (1d6 + {}) slashing damage.".format(self.find_attk_mod(self.modifiers[1]), self.find_damage(6, self.modifiers[1]), self.modifiers[1]),
            "Light Scrossbow": "<i>Ranged Weapon Attack</i>: +{} to hit, range 80/320 ft., one target. <i>Hit</i>: {} (1d8 + {}) piercing damage.".format(self.find_attk_mod(self.modifiers[1]), self.find_damage(8, self.modifiers[1]), self.modifiers[1])
        }
        self.inventory = {"leather armor", "scimitar", "light crossbow"}
        self.vulnerable = []
        self.dmg_resist = []
        self.cond_resist = []
        self.dmg_immune = []
        self.cond_immune = []
