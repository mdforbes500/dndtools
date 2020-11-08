#!/usr/bin/python3

import random
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
        self.abil_mods = {
            "str": 0,
            "dex": 0,
            "con": 0,
            "int": 0,
            "wis": 0,
            "cha": 0
        }
        self.features = {}
        self.actions = {}
        self.nat_armor = 0
        self.vulnerable = []
        self.skills = {}
        self.speed = {}
        self.senses = {}
        self.dmg_immune = []
        self.dmg_resist = []
        self.languages = []
        self.cond_immune = []

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
        self.abil_mods["dex"] = 2
        self.abil_mods["wis"] = 2
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
        self.abil_mods["int"] = -2
        self.abil_mods["cha"] = -2
        self.features["Amphibious"] = "The bullywug can breathe air and water."
        self.features["Speak with Frogs and Toads"] = "The bullywug can communicate simple concepts to frogs and toads when it speaks in Bullywug."
        self.features["Swamp Camouflage"] = "The bullywug has advantage on Dexterity (Stealth) checks made to hide in swampy terrain."
        self.features["Standing Leap"] = "The bullywug's long jump is up to 20 feet and its high jump is up to 10 feet, with or without a running start."
        self.speed["ground"] = 20
        self.speed["swim"] = 40
        self.languages.append("Bullywug")

class Dragonborn(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(dragonborn)"
        self.abil_mods["str"] = 2
        self.abil_mods["cha"] = 1

        breath_dc = 8 + template.modifiers[2] + template.proficiency
        if template.cr <= 6:
            damage = 2
        elif template.cr > 6 and template.cr <= 11:
            damage = 4
        else:
            damage = 5

        roll = random.randint(1,10)
        if roll == 1:
            self.features["Draconic Ancestry"] = "The dragonborn has black dragon ancestry."
            self.features["Breath Weapon"] = "The dragonborn can use its action to spit acid. When they use their breath weapon, each creature in a 5 by 30 ft. line must make a Dexterity saving throw (DC {}). A creature takes {}d6 acid damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
            self.features["Damage Resistance"] = "The dragonborn has resistance to acid damage."
        elif roll == 2:
            self.features["Draconic Ancestry"] = "The dragonborn has blue dragon ancestry."
            self.features["Breath Weapon"] = "The dragonborn can use its action to shoot lightning. When they use their breath weapon, each creature in a 5 by 30 ft. line must make a Dexterity saving throw (DC {}). A creature takes {}d6 lightning damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
            self.features["Damage Resistance"] = "The dragonborn has resistance to lightning damage."
        elif roll == 3:
            self.features["Draconic Ancestry"] = "The dragonborn has brass dragon ancestry."
            self.features["Breath Weapon"] = "The dragonborn can use its action to breathe fire. When they use their breath weapon, each creature in a 5 by 30 ft. line must make a Dexterity saving throw (DC {}). A creature takes {}d6 fire damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
            self.features["Damage Resistance"] = "The dragonborn has resistance to fire damage."
        elif roll == 4:
            self.features["Draconic Ancestry"] = "The dragonborn has bronze dragon ancestry."
            self.features["Breath Weapon"] = "The dragonborn can use its action to shoot lightning. When they use their breath weapon, each creature in a 5 by 30 ft. line must make a Dexterity saving throw (DC {}). A creature takes {}d6 lightning damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
            self.features["Damage Resistance"] = "The dragonborn has resistance to lightning damage."
        elif roll == 5:
            self.features["Draconic Ancestry"] = "The dragonborn has copper dragon ancestry."
            self.features["Breath Weapon"] = "The dragonborn can use its action to spit acid. When they use their breath weapon, each creature in a 5 by 30 ft. line must make a Dexterity saving throw (DC {}). A creature takes {}d6 acid damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
            self.features["Damage Resistance"] = "The dragonborn has resistance to acid damage."
        elif roll == 6:
            self.features["Draconic Ancestry"] = "The dragonborn has gold dragon ancestry."
            self.features["Breath Weapon"] = "The dragonborn can use its action to breathe fire. When they use their breath weapon, each creature in a 15 ft. cone must make a Dexterity saving throw (DC {}). A creature takes {}d6 fire damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
            self.features["Damage Resistance"] = "The dragonborn has resistance to fire damage."
        elif roll == 7:
            self.features["Draconic Ancestry"] = "The dragonborn has green dragon ancestry."
            self.features["Breath Weapon"] = "The dragonborn can use its action to exhale a cloud of posion. When they use their breath weapon, each creature in a 15 ft. cone must make a Constitution saving throw (DC {}). A creature takes {}d6 posion damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
            self.features["Damage Resistance"] = "The dragonborn has resistance to posion damage."
        elif roll == 8:
            self.features["Draconic Ancestry"] = "The dragonborn has red dragon ancestry."
            self.features["Breath Weapon"] = "The dragonborn can use its action to breathe fire. When they use their breath weapon, each creature in a 15 ft. cone must make a Dexterity saving throw (DC {}). A creature takes {}d6 fire damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
            self.features["Damage Resistance"] = "The dragonborn has resistance to fire damage."
        elif roll == 9:
            self.features["Draconic Ancestry"] = "The dragonborn has silver dragon ancestry."
            self.features["Breath Weapon"] = "The dragonborn can use its action to exhale a blast of cold. When they use their breath weapon, each creature in a 15 ft. cone must make a Constitution saving throw (DC {}). A creature takes {}d6 cold damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
            self.features["Damage Resistance"] = "The dragonborn has resistance to cold damage."
        else:
            self.features["Draconic Ancestry"] = "The dragonborn has white dragon ancestry."
            self.features["Breath Weapon"] = "The dragonborn can use its action to exhale a blast of cold. When they use their breath weapon, each creature in a 15 ft. cone must make a Constitution saving throw (DC {}). A creature takes {}d6 cold damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
            self.features["Damage Resistance"] = "The dragonborn has resistance to cold damage."
        self.languages.append("Draconic")

class Drow(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(elf)"
        self.alignment_center = "neutral evil"
        self.abil_mods["dex"] = 2
        self.abil_mods["cha"] = 1
        self.features["Fey Ancestry"] = "The drow has advantage on saving throws against being charmed, and magic can't put them to sleep."
        self.features["Innate Spellcasting"] = "The drow's spellcasting ability is Charisma (spell save DC {}). It can innately cast the following spells, requiring no material components:\n\nAt will: <i>dancing lights</i>\n1/day each: <i>darkness, faerie fire</i>".format(8 + template.proficiency + template.modifiers[5])
        self.features["Sunlight Sensitivity"] = "While in sunlight, the drow has disadvantage on attack rolls, as well as on Wisdon (Perception) checks that rely on sight."
        self.senses["darkvision"] = "{} ft.".format(120)
        self.languages.append("Elvish")
        self.languages.append("Undercommon")

class HillDwarf(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(dwarf)"
        self.abil_mods["wis"] = 2
        self.abil_mods["con"] = 2
        self.features["Dwarven Resilience"] = "The dwarf has advantage on saving throws against poison, and has resistance against poison damage."
        self.features["Stonecunning"] = "Whenever the dwarf makes an Intelligence (History) check related to the origin of stonework, the dwarf is considered proficient in the History skill and adds double the proficiency bonus to the check, instead of the dwarf's normal proficiency bonus."
        self.speed["ground"] = 25
        self.senses["darkvision"] = 60
        self.languages.append("Dwarvish")

class MountainDwarf(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(dwarf)"
        self.abil_mods["str"] = 2
        self.abil_mods["con"] = 2
        self.features["Dwarven Resilience"] = "The dwarf has advantage on saving throws against poison, and has resistance against poison damage."
        self.features["Stonecunning"] = "Whenever the dwarf makes an Intelligence (History) check related to the origin of stonework, the dwarf is considered proficient in the History skill and adds double the proficiency bonus to the check, instead of the dwarf's normal proficiency bonus."
        self.speed["ground"] = 25
        self.senses["darkvision"] = 60
        self.languages.append("Dwarvish")

class WoodElf(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(elf)"
        self.abil_mods["wis"] = 1
        self.abil_mods["dex"] = 2
        self.features["Fey Ancestry"] = "The elf has advantage on saving throws against being charmed, and magic can't put the elf to sleep."
        self.features["Trance"] = "Elves don't need to sleep. Instead they meditate deeply, reamining semiconscious, for 4 hours a day. While meditating, the elf can dream after a fashion; such dreams are actually mental exercisesthat have become reflexive through years of practice. After resting in this way, the elf gains the same benefit that a human does from 8 hours of sleep."
        self.senses["darkvision"] = 60
        self.skills["Perception"] = template.proficiency + template.modifiers[4]
        self.languages.append("Elvish")

class HighElf(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(elf)"
        self.abil_mods["int"] = 1
        self.abil_mods["dex"] = 2
        self.features["Fey Ancestry"] = "The elf has advantage on saving throws against being charmed, and magic can't put the elf to sleep."
        self.features["Trance"] = "Elves don't need to sleep. Instead they meditate deeply, reamining semiconscious, for 4 hours a day. While meditating, the elf can dream after a fashion; such dreams are actually mental exercisesthat have become reflexive through years of practice. After resting in this way, the elf gains the same benefit that a human does from 8 hours of sleep."
        self.senses["darkvision"] = 60
        self.skills["Perception"] = template.proficiency + template.modifiers[4]
        self.languages.append("Elvish")

class Gnoll(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(gnoll)"
        self.abil_mods["str"] = 2
        self.abil_mods["int"] = -2
        self.features["Rampage"] = "When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack."
        self.senses["darkvision"] = 60

class RockGnome(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Small"
        self.type = "humanoid"
        self.race = "(gnome)"
        self.abil_mods["con"] = 2
        self.abil_mods["int"] = 2
        self.features["Gnome Cunning"] = "The gnome has advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
        self.features["Innate Spellcasting"] = "The gnome's innate spellcasting ability is Intelligence (spell save DC {}). It can innately cast the following spells, requiring no material components:\n\nAt will: <i>nondetection</i> (self only)\n1/day each: <i>blindness/deafness, blur, disguise self</i>".format(8 + template.proficiency + template.modifiers[3])
        self.speed["ground"] = 25
        self.senses["darkvision"] = 60
        self.languages.append("Gnomish")

class ForestGnome(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Small"
        self.type = "humanoid"
        self.race = "(gnome)"
        self.abil_mods["dex"] = 2
        self.abil_mods["int"] = 2
        self.features["Gnome Cunning"] = "The gnome has advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
        self.features["Innate Spellcasting"] = "The gnome's innate spellcasting ability is Intelligence (spell save DC {}). It can innately cast the following spells, requiring no material components:\n\nAt will: <i>nondetection</i> (self only)\n1/day each: <i>blindness/deafness, blur, disguise self</i>".format(8 + template.proficiency + template.modifiers[3])
        self.speed["ground"] = 25
        self.senses["darkvision"] = 60
        self.languages.append("Gnomish")

class DeepGnome(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Small"
        self.type = "humanoid"
        self.race = "(gnome)"
        self.abil_mods["str"] = 1
        self.abil_mods["dex"] = 2
        self.features["Gnome Cunning"] = "The gnome has advantage on Intelligence, Widsom and Charisma saving throws against magic."
        self.features["Innate Spellcasting"] = "The gnome's innate spellcasting ability is Intelligence (spell save DC {}). It can innately cast the following spells, requiring no material components:\n\nAt will: <i>nondetection</i> (self only)\n1/day each: <i>blindness/deafness, blur, disguise self</i>".format(8 + template.proficiency + template.modifiers[3])
        self.features["Stone Camouflage"] = "The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
        self.speed["ground"] = 20
        self.senses["darkvision"] = 120
        self.languages.append("Gnomish")
        self.languages.append("Terran")
        self.languages.append("Undercommon")

class Goblin(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Small"
        self.type = "humanoid"
        self.race = "(goblinoid)"
        self.abil_mods["str"] = -2
        self.abil_mods["dex"] = 2
        self.features["Nimble Escape"] = "The goblin can take the Disengage or Hide action as a bonus action on each of its turns."
        self.senses["darkvision"] = 60
        self.languages.append("Goblin")

class Grimlock(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(grimlock)"
        self.abil_mods["str"] = 2
        self.abil_mods["cha"] = -2
        self.features["Blind Senses"] = "The grimlock can't use its blindsight while deafened and unable to smell."
        self.features["Keen Hearing and Smell"] = "The grimlock has advantage on Wisdom (Perception) checks that rely on hearing or smell."
        self.features["Stone Camouflage"] = "The grimlock has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
        self.cond_immune = ["blinded"]
        self.senses["blindsight"] = "30 ft., or 10 ft., while deafened (blind beyond this radius)"
        self.languages.append("Undercommon")

class HalfElf(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(half-elf)"
        self.abil_mods["dex"] = 1
        self.abil_mods["int"] = 1
        self.abil_mods["cha"] = 2
        skills = [
            ["Athletics", template.modifiers[0]],
            ["Acrobatics", template.modifiers[0]],
            ["Sleight of Hand", template.modifiers[1]],
            ["Stealth", template.modifiers[1]],
            ["Arcana", template.modifiers[3]],
            ["History", template.modifiers[3]],
            ["Investigation", template.modifiers[3]],
            ["Nature", template.modifiers[3]],
            ["Religion", template.modifiers[3]],
            ["Animal Handling", template.modifiers[4]],
            ["Insight", template.modifiers[4]],
            ["Medicine", template.modifiers[4]],
            ["Percpetion", template.modifiers[4]],
            ["Survival", template.modifiers[4]],
            ["Deception", template.modifiers[5]],
            ["Intimidation", template.modifiers[5]],
            ["Performance", template.modifiers[5]],
            ["Persuasion", template.modifiers[5]]
        ]
        rand1 = random.randint(0, len(skills)-1)
        rand2 = random.randint(0, len(skills)-1)
        self.skills[skills[rand1][0]] = skills[rand1][1] + template.proficiency
        self.skills[skills[rand2][0]] = skills[rand2][1] + template.proficiency
        self.languages.append("Elvish")

class HalfOrc(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(half-orc)"
        self.abil_mods["str"] = 2
        self.abil_mods["con"] = 1
        self.features["Relentless Endurance"] = "When the half-orc is reduced to 0 hit points but not killed outright, the half-orc can drop to 1 hit point instead. This feature can't be used again until the half-orc finishes a long rest. "
        self.senses["darkvision"] = 60
        self.skills["Intimidation"] = template.proficiency + template.modifiers[5]
        self.languages.append("Orcish")

class LightfootHalfling(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Small"
        self.type = "humanoid"
        self.race = "(halfling)"
        self.abil_mods["dex"] = 2
        self.abil_mods["cha"] = 1
        self.features["Brave"] = "The halfling has advantage on saving throws against being frightened."
        self.features["Halfling Nimbleness"] = "The halfling can move through the space of any creature that is of a size larger than their own."
        self.features["Lucky"] = "When the halfling rolls a 1 on the d20 for an attack roll, ability check, or saving throw, the halfling can reroll the die and must use the new roll."
        self.speed["ground"] = 25
        self.languages.append("Halfling")

class StoutHalfling(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Small"
        self.type = "humanoid"
        self.race = "(halfling)"
        self.abil_mods["dex"] = 2
        self.abil_mods["con"] = 1
        self.features["Brave"] = "The halfling has advantage on saving throws against being frightened."
        self.features["Halfling Nimbleness"] = "The halfling can move through the space of any creature that is of a size larger than their own."
        self.features["Lucky"] = "When the halfling rolls a 1 on the d20 for an attack roll, ability check, or saving throw, the halfling can reroll the die and must use the new roll."
        self.speed["ground"] = 25
        self.languages.append("Halfling")

class Hobgoblin(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(goblinoid)"
        self.features["Martial Advantage"] = "Once per turn, the hobgoblin can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated."
        self.senses["darkvision"] = 60
        self.languages.append("Goblin")

class Kenku(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(kenku)"
        self.abil_mods["dex"] = 2
        self.features["Ambusher"] = "In the first round of combat, the kenku has advantage on attack rolls against any creature it surprised."
        self.features["Mimicry"] = "The kenku can mimic any sounds it has heard, including voices. A creature that hears the sounds can tell they are imitations with a successful DC 14 Wisdom (Insight) check."
        self.languages = ["understands Common and Auran but speaks only through the use of its Mimicry trait"]

class Kobold(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Small"
        self.type = "humanoid"
        self.race = "(kobold)"
        self.abil_mods["str"] = -4
        self.abil_mods["dex"] = 2
        self.features["Pack Tactics"] = "The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated."
        self.features["Sunlight Sensitivity"] = "While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
        self.senses["darkvision"] = 60
        self.languages.append("Draconic")

class KuoToa(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(kuo-toa)"
        self.features["Amphibious"] = "The kuo-toa can breathe air and water."
        self.features["Otherworldly Perception"] = "The kuo-toa can sense the presence of any creature within 30 feet of it that is invisible or on the Ethereal Plane. It can pinpoint such a creature that is moving."
        self.features["Slippery"] = "The kuo-toa has advantage on ability checks and saving throws made to escape a grapple."
        self.features["Sunlight Sensitivity"] = "While in sunlight, the kuo-toa has disadvantage on attack rolls, as well as Wisdom (Perception) checks that rely on sight."
        self.speed["ground"] = 30
        self.speed["swim"] = 30
        self.senses["darkvision"] = 120
        self.languages.append("Undercommon")

class Lizardfolk(Race): #FIXME

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(lizardfolk)"
        self.abil_mods["str"] = 2
        self.abil_mods["int"] = -2
        self.features["Hold Breath"] = "The lizardfolk can hold its breath for 15 minutes."
        self.nat_armor = 3
        self.speed["ground"] = 30
        self.speed["swim"] = 30
        self.languages.append("Draconic")

class Merfolk(Race): #FIXME

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(merfolk)"
        self.features["Amphibious"] = "The merfolk can breathe air and water."
        self.speed["ground"] = 10
        self.speed["swim"] = 40
        self.languages.append("Aquan")

class Orc(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(orc)"
        self.abil_mods["str"] = 2
        self.abil_mods["int"] = -2
        self.features["Aggressive"] = "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see."
        self.senses["darkvision"] = 60
        self.languages.append("Orc")

class Skeleton(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.type = "undead"
        self.race = None
        self.abil_mods["dex"] = 2
        self.abil_mods["int"] = -4
        self.abil_mods["cha"] = -4
        self.senses["darkvision"] = 60
        self.languages = ["understands all languages it knew in life but can't speak"]
        self.vulnerable.append("bludgeoning")
        self.dmg_immune.append("poision")
        self.cond_immune.append("exhausted", "poisoned")

class Tiefling(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(tiefling)"
        self.abil_mods["int"] = 1
        self.abil_mods["cha"] = 2
        if template.cr < 3:
            self.features["Infernal Legacy"] = "The tiefling knows the <i>thaumaturgy</i> cantrip. Charisma is the casting modifier for this spell."
        elif template.cr >= 3 and template.cr < 5:
            self.features["Infernal Legacy"] = "The tiefling knows the <i>thaumaturgy</i> cantrip, and can cast <i>hellish rebuke</i> as a 2nd-level spell once per long rest. Charisma is the casting modifier for this spell."
        else:
            self.features["Infernal Legacy"] = "The tiefling knows the <i>thaumaturgy</i> cantrip, <i>hellish rebuke</i> as a 2nd-level spell once per long rest, and they can cast <i>darkness</i> once per long rest. Charisma is the casting modifier for this spell."
        self.dmg_resist.append("fire")
        self.senses["darkvision"] = 60
        self.languages.append("Infernal")

class Troglodyte(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(troglodyte)"
        self.abil_mods["str"] = 2
        self.abil_mods["con"] = 2
        self.abil_mods["int"] = -4
        self.abil_mods["cha"] = -4
        self.features["Chameleon Skin"] = "The troglodyte has advantage on Dexterity (stealth) checks made to hide."
        self.features["Stench"] = "Any creature other than a troglodyte that starts its turn within 5 feet of the troglodyte must succeed a DC 12 Constitution saving throw of be poisoned until the start of the creature's next turn. On a successful saving throw, the creature is immune to the stench of all troglodytes for 1 hour."
        self.features["Sunlight Sensitivity"] = "While in the sunlight, the troglodyte has disadvantage on attack rolls, as well as Wisdom (Perception) checks that rely on sight."
        self.nat_armor = 1
        self.senses["darkvision"] = 60
        self.languages.append("Troglodyte")

class Zombie(Race):

    def __init__(self, template: npc.NPC) -> None:
        """
        Takes an NPC template and alters it to have the racial abilities given in
        the DM's Guide.
        """
        self.type = "undead"
        self.race = None
        self.abil_mods["str"] = 1
        self.abil_mods["con"] = 2
        self.abil_mods["int"] = -6
        self.abil_mods["wis"] = -4
        self.abil_mods["cha"] = -4
        self.features["Undead Fortitude"] = "If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie drops to 1 hit point instead."
        self.senses["darkvision"] = 60
        self.languages = ["understands all languages it knew in life but can't speak"]
        self.vulnerable.append("bludgeoning")
        self.dmg_immune.append("poision")
        self.cond_immune.append("poisoned")
