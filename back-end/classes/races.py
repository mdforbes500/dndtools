#!/usr/bin/python
import random
import classes.npc as npc

def aarakocra(obj: npc.NPC) -> None:
    """
    Takes an NPC template and alters it to have the racial abilities given in
    the DM's Guide.
    """
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(aarakocra)"
    obj.abilities[1] += 2 # +2 to Dex
    obj.abilities[4] += 2 # +2 to Wis
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Dive Attack"] = "If the aarakocra is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 3 (1d6) damage to the target"
    obj.actions["Talon"] = ['Melee',
        obj.find_attk_mod(obj.modifiers[0]),
        5,
        obj.find_damage(4, obj.modifiers[0]),
        '1d4 + {}'.format(obj.modifiers[0]), 'piercing']
    obj.speed["ground"] = 20
    obj.speed["fly"] = 50
    obj.languages.append("Auran")

def bullywug(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(bullywug)"
    obj.abilities[3] -= 2 # -2 to Int
    obj.abilities[5] -= 2 # -2 to Cha
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Amphibious"] = "The bullywug can breathe air and water."
    obj.features["Speak with Frogs and Toads"] = "The bullywug can communicate simple concepts to frogs and toads when it speaks in Bullywug."
    obj.features["Swamp Camouflage"] = "The bullywug has advantage on Dexterity (Stealth) checks made to hide in swampy terrain."
    obj.features["Standing Leap"] = "The bullywug's long jump is up to 20 feet and its high jump is up to 10 feet, with or without a running start."
    obj.speed["ground"] = 20
    obj.speed["swim"] = 40
    obj.langauges.append("Bullywug")

def dragonborn(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(dragonborn)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[5] += 1 # +1 to Cha
    obj.update_modifiers()
    obj.update_perception()
    roll = math.randint(1,10)
    breath_dc = 8 + obj.modifiers[2] + obj.proficiency
    if obj.cr <= 6:
        damage = 2
    elif obj.cr > 6 and obj.cr <= 11:
        damage = 4
    else:
        damage = 5
    if roll == 1:
        obj.features["Draconic Ancestry"] = "The dragonborn has black dragon ancestry."
        obj.features["Breath Weapon"] = "The dragonborn can use its action to spit acid. When they use their breath weapon, each creature in a 5 by 30 ft. line must make a Dexterity saving throw (DC {}). A creature takes {}d6 acid damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
        obj.features["Damage Resistance"] = "The dragonborn has resistance to acid damage."
    elif roll == 2:
        obj.features["Draconic Ancestry"] = "The dragonborn has blue dragon ancestry."
        obj.features["Breath Weapon"] = "The dragonborn can use its action to shoot lightning. When they use their breath weapon, each creature in a 5 by 30 ft. line must make a Dexterity saving throw (DC {}). A creature takes {}d6 lightning damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
        obj.features["Damage Resistance"] = "The dragonborn has resistance to lightning damage."
    elif roll == 3:
        obj.features["Draconic Ancestry"] = "The dragonborn has brass dragon ancestry."
        obj.features["Breath Weapon"] = "The dragonborn can use its action to breathe fire. When they use their breath weapon, each creature in a 5 by 30 ft. line must make a Dexterity saving throw (DC {}). A creature takes {}d6 fire damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
        obj.features["Damage Resistance"] = "The dragonborn has resistance to fire damage."
    elif roll == 4:
        obj.features["Draconic Ancestry"] = "The dragonborn has bronze dragon ancestry."
        obj.features["Breath Weapon"] = "The dragonborn can use its action to shoot lightning. When they use their breath weapon, each creature in a 5 by 30 ft. line must make a Dexterity saving throw (DC {}). A creature takes {}d6 lightning damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
        obj.features["Damage Resistance"] = "The dragonborn has resistance to lightning damage."
    elif roll == 5:
        obj.features["Draconic Ancestry"] = "The dragonborn has copper dragon ancestry."
        obj.features["Breath Weapon"] = "The dragonborn can use its action to spit acid. When they use their breath weapon, each creature in a 5 by 30 ft. line must make a Dexterity saving throw (DC {}). A creature takes {}d6 acid damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
        obj.features["Damage Resistance"] = "The dragonborn has resistance to acid damage."
    elif roll == 6:
        obj.features["Draconic Ancestry"] = "The dragonborn has gold dragon ancestry."
        obj.features["Breath Weapon"] = "The dragonborn can use its action to breathe fire. When they use their breath weapon, each creature in a 15 ft. cone must make a Dexterity saving throw (DC {}). A creature takes {}d6 fire damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
        obj.features["Damage Resistance"] = "The dragonborn has resistance to fire damage."
    elif roll == 7:
        obj.features["Draconic Ancestry"] = "The dragonborn has green dragon ancestry."
        obj.features["Breath Weapon"] = "The dragonborn can use its action to exhale a cloud of posion. When they use their breath weapon, each creature in a 15 ft. cone must make a Constitution saving throw (DC {}). A creature takes {}d6 posion damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
        obj.features["Damage Resistance"] = "The dragonborn has resistance to posion damage."
    elif roll == 8:
        obj.features["Draconic Ancestry"] = "The dragonborn has red dragon ancestry."
        obj.features["Breath Weapon"] = "The dragonborn can use its action to breathe fire. When they use their breath weapon, each creature in a 15 ft. cone must make a Dexterity saving throw (DC {}). A creature takes {}d6 fire damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
        obj.features["Damage Resistance"] = "The dragonborn has resistance to fire damage."
    elif roll == 9:
        obj.features["Draconic Ancestry"] = "The dragonborn has silver dragon ancestry."
        obj.features["Breath Weapon"] = "The dragonborn can use its action to exhale a blast of cold. When they use their breath weapon, each creature in a 15 ft. cone must make a Constitution saving throw (DC {}). A creature takes {}d6 cold damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
        obj.features["Damage Resistance"] = "The dragonborn has resistance to cold damage."
    else:
        obj.features["Draconic Ancestry"] = "The dragonborn has white dragon ancestry."
        obj.features["Breath Weapon"] = "The dragonborn can use its action to exhale a blast of cold. When they use their breath weapon, each creature in a 15 ft. cone must make a Constitution saving throw (DC {}). A creature takes {}d6 cold damage on a failed save, and half as much damage on a sucessful one. After the dragonborn uses their breath weapon, it can't be used again until they complete a short or long rest.".format(breath_dc, damage)
        obj.features["Damage Resistance"] = "The dragonborn has resistance to cold damage."
    obj.langauges.append("Draconic")

def drow(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(elf)"
    obj.abilities[1] += 2 # +2 to Dex
    obj.abilities[5] += 1 # +1 to Cha
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Fey Ancestry"] = "The drow has advantage on saving throws against being charmed, and magic can't put them to sleep."
    obj.features["Innate Spellcasting"] = "The drows's spellcasting ability is Charisma (spell save DC {}). It can innately cast the following spells, requiring no material components:\n\nAt will: <i>dancing lights</i>\n1/day each: <i>darkness, faerie fire</i>".format(8 + obj.proficiency + obj.madifiers[5])
    obj.features["Sunlight Sensitivity"] = "While in sunlight, the drow has disadvantage on attack rolls, as well as on Wisdon (Perception) checks that rely on sight."
    obj.senses["darkvision"] = 120
    obj.languages.append("Elvish")
    obj.languages.append("Undercommon")

def hill_dwarf(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(dwarf)"
    obj.abilities[4] += 2 # +2 to Wis
    obj.abilities[2] += 2 # +2 to Con
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Dwarven Resilience"] = "The dwarf has advantage on saving throws against poison, and has resistance against poison damage."
    obj.features["Stonecunning"] = "Whenever the dwarf makes an Intelligence (History) check related to the origin of stonework, the dwarf is considered proficient in the History skill and adds double the proficiency bonus to the check, instead of the dwarf's normal proficiency bonus."
    obj.speed["ground"] = 25
    obj.senses["darkvision"] = 60
    obj.languages.append("Dwarvish")

def mountain_dwarf(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(dwarf)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[2] += 2 # +2 to Con
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Dwarven Resilience"] = "The dwarf has advantage on saving throws against poison, and has resistance against poison damage."
    obj.features["Stonecunning"] = "Whenever the dwarf makes an Intelligence (History) check related to the origin of stonework, the dwarf is considered proficient in the History skill and adds double the proficiency bonus to the check, instead of the dwarf's normal proficiency bonus."
    obj.speed["ground"] = 25
    obj.senses["darkvision"] = 60
    obj.languages.append("Dwarvish")

def wood_elf(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(elf)"
    obj.abilities[4] += 1 # +1 to Wis
    obj.abilities[1] += 2 # +2 to Dex
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Fey Ancestry"] = "The elf has advantage on saving throws against being charmed, and magic can't put the elf to sleep."
    obj.features["Trance"] = "Elves don't need to sleep. Instead they meditate deeply, reamining semiconscious, for 4 hours a day. While meditating, the elf can dream after a fashion; such dreams are actually mental exercisesthat have become reflexive through years of practice. After resting in this way, the elf gains the same benefit that a human does from 8 hours of sleep."
    obj.senses["darkvision"] = 60
    obj.skills["Perception"] = obj.proficiency + obj.modifiers[4]
    obj.languages.append("Elvish")

def high_elf(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(elf)"
    obj.abilities[3] += 1 # +1 to Int
    obj.abilities[1] += 2 # +2 to Dex
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Fey Ancestry"] = "The elf has advantage on saving throws against being charmed, and magic can't put the elf to sleep."
    obj.features["Trance"] = "Elves don't need to sleep. Instead they meditate deeply, reamining semiconscious, for 4 hours a day. While meditating, the elf can dream after a fashion; such dreams are actually mental exercisesthat have become reflexive through years of practice. After resting in this way, the elf gains the same benefit that a human does from 8 hours of sleep."
    obj.senses["darkvision"] = 60
    obj.skills["Perception"] = obj.proficiency + obj.modifiers[4]
    obj.languages.append("Elvish")

def gnoll(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(gnoll)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[3] -= 2 # -2 to Int
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Rampage"] = "When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack."
    obj.senses["darkvision"] = 60

def rock_gnome(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(gnome)"
    obj.abilities[2] += 2 # +2 to Con
    obj.abilities[3] += 2 # +2 to Int
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Gnome Cunning"] = "The gnome has advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
    obj.features["Innate Spellcasting"] = "The gnome's innate spellcasting ability is Intelligence (spell save DC {}). It can innately cast the following spells, requiring no material components:\n\nAt will: <i>nondetection</i> (self only)\n1/day each: <i>blindness/deafness, blur, disguise self</i>".format(8 + obj.proficiency + obj.modifiers[3])
    obj.speed["ground"] = 25
    obj.senses["darkvision"] = 60
    obj.languages.append("Gnomish")

def forest_gnome(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(gnome)"
    obj.abilities[1] += 2 # +2 to Dex
    obj.abilities[3] += 2 # +2 to Int
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Gnome Cunning"] = "The gnome has advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
    obj.features["Innate Spellcasting"] = "The gnome's innate spellcasting ability is Intelligence (spell save DC {}). It can innately cast the following spells, requiring no material components:\n\nAt will: <i>nondetection</i> (self only)\n1/day each: <i>blindness/deafness, blur, disguise self</i>".format(8 + obj.proficiency + obj.modifiers[3])
    obj.speed["ground"] = 25
    obj.senses["darkvision"] = 60
    obj.languages.append("Gnomish")

def deep_gnome(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(gnome)"
    obj.abilities[0] += 1 # +1 to Str
    obj.abilities[1] += 2 # +2 to Dex
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Gnome Cunning"] = "The gnome has advantage on Intelligence, Widsom and Charisma saving throws against magic."
    obj.features["Innate Spellcasting"] = "The gnome's innate spellcasting ability is Intelligence (spell save DC {}). It can innately cast the following spells, requiring no material components:\n\nAt will: <i>nondetection</i> (self only)\n1/day each: <i>blindness/deafness, blur, disguise self</i>".format(8 + obj.proficiency + obj.modifiers[3])
    obj.features["Stone Camouflage"] = "The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
    obj.speed["ground"] = 20
    obj.senses["darkvision"] = 120
    obj.langauges.append("Gnomish")
    obj.langauges.append("Terran")
    obj.langauges.append("Undercommon")

def goblin(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(goblinoid)"
    obj.abilities[0] -= 2 # -2 to Str
    obj.abilities[1] += 2 # +2 to Dex
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Nimble Escape"] = "The goblin can take the Disengage or Hide action as a bonus action on each of its turns."
    obj.senses["darkvision"] = 60
    obj.languages.append("Goblin")

def grimlock(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(grimlock)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[5] -= 2 # -2 to Cha
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Blind Senses"] = "The grimlock can't use its blindsight while deafened and unable to smell."
    obj.features["Keen Hearing and Smell"] = "The grimlock has advantage on Wisdom (Perception) checks that rely on hearing or smell."
    obj.features["Stone Camouflage"] = "The grimlock has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
    obj.cond_immune = ["blinded"]
    obj.senses["blindsight"] = "30 ft., or 10 ft., while deafened (blind beyond this radius)"
    obj.languages.append("Undercommon")

def half_elf(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(half-elf)"
    obj.abilities[1] += 1 # +2 to Dex
    obj.abilities[3] += 1 # +2 to Int
    obj.abilities[5] += 2 # +2 to Cha
    obj.update_modifiers()
    obj.update_perception()
    skills = [
        ["Athletics", obj.modifiers[0]],
        ["Acrobatics", obj.modifiers[0]],
        ["Sleight of Hand", obj.modifiers[1]],
        ["Stealth", obj.modifiers[1]],
        ["Arcana", obj.modifiers[3]],
        ["History", obj.modifiers[3]],
        ["Investigation", obj.modifiers[3]],
        ["Nature", obj.modifiers[3]],
        ["Religion", obj.modifiers[3]],
        ["Animal Handling", obj.modifiers[4]],
        ["Insight", obj.modifiers[4]],
        ["Medicine", obj.modifiers[4]],
        ["Percpetion", obj.modifiers[4]],
        ["Survival", obj.modifiers[4]],
        ["Deception", obj.modifiers[5]],
        ["Intimidation", obj.modifiers[5]],
        ["Performance", obj.modifiers[5]],
        ["Persuasion", obj.modifiers[5]]
    ]
    rand1 = math.randint(0, len(skills)-1)
    rand2 = math.randint(0, len(skills)-1)
    obj.skills[skills[rand1][0]] = skills[rand1][1] + obj.proficiency
    obj.skills[skills[rand2][0]] = skills[rand2][1] + obj.proficiency
    obj.languages.append("Elvish")

def half_orc(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(half-orc)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[2] += 1 # +1 to Con
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Relentless Endurance"] = "When the half-orc is reduced to 0 hit points but not killed outright, the half-orc can drop to 1 hit point instead. This feature can't be used again until the half-orc finishes a long rest. "
    obj.senses["darkvision"] = 60
    obj.skills["Intimidation"] = obj.proficiency + obj.modifiers[5]
    obj.languages.append("Orcish")

def lightfoot_halfling(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(halfling)"
    obj.abilities[1] += 2 # +2 to Dex
    obj.abilities[5] += 1 # +1 to Cha
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Brave"] = "The halfling has advantage on saving throws against being frightened."
    obj.features["Halfling Nimbleness"] = "The halfling can move through the space of any creature that is of a size larger than their own."
    obj.features["Lucky"] = "When the halfling rolls a 1 on the d20 for an attack roll, ability check, or saving throw, the halfling can reroll the die and must use the new roll."
    obj.speed["ground"] = 25
    obj.languages.append("Halfling")

def stout_halfling(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(halfling)"
    obj.abilities[1] += 2 # +2 to Dex
    obj.abilities[2] += 1 # +1 to Con
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Brave"] = "The halfling has advantage on saving throws against being frightened."
    obj.features["Halfling Nimbleness"] = "The halfling can move through the space of any creature that is of a size larger than their own."
    obj.features["Lucky"] = "When the halfling rolls a 1 on the d20 for an attack roll, ability check, or saving throw, the halfling can reroll the die and must use the new roll."
    obj.speed["ground"] = 25
    obj.languages.append("Halfling")

def hobgoblin(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(goblinoid)"
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Martial Advantage"] = "Once per turn, the hobgoblin can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated."
    obj.senses["darkvision"] = 60
    obj.langauges.append("Goblin")

def kenku(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(kenku)"
    obj.abilities[1] += 2 # +2 to Dex
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Ambusher"] = "In the first round of combat, the kenku has advantage on attack rolls against any creature it surprised."
    obj.features["Mimicry"] = "The kenku can mimic any sounds it has heard, including voices. A creature that hears the sounds can tell they are imitations with a successful DC 14 Wisdom (Insight) check."
    obj.langagues = ["understands Common and Auran but speaks only through the use of its Mimicry trait"]

def kobold(obj):
    obj.size = "Small"
    obj.type = "humanoid"
    obj.race = "(kobold)"
    obj.abilities[0] -= 4 # -4 to Str
    obj.abilities[1] += 2 # +2 to Dex
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Pack Tactics"] = "The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated."
    obj.features["Sunlight Sensitivity"] = "While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
    obj.senses["darkvision"] = 60
    obj.languages.append("Draconic")

def kuo_toa(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(kuo-toa)"
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Amphibious"] = "The kuo-toa can breathe air and water."
    obj.features["Otherworldly Perception"] = "The kuo-toa can sense the presence of any creature within 30 feet of it that is invisible or on the Ethereal Plane. It can pinpoint such a creature that is moving."
    obj.features["Slippery"] = "The kuo-toa has advantage on ability checks and saving throws made to escape a grapple."
    obj.features["Sunlight Sensitivity"] = "While in sunlight, the kuo-toa has disadvantage on attack rolls, as well as Wisdom (Perception) checks that rely on sight."
    obj.speed["ground"] = 30
    obj.speed["swim"] = 30
    obj.senses["darkvision"] = 120
    obj.languages.append("Undercommon")

def lizardfolk(obj): #FIXME
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(lizardfolk)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[3] -= 2 # -2 to Int
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Hold Breath"] = "The lizardfolk can hold its breath for 15 minutes."
    obj.armor += 3
    obj.speed["ground"] = 30
    obj.speed["swim"] = 30
    obj.languages.append("Draconic")

def merfolk(obj): #FIXME
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(merfolk)"
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Amphibious"] = "The merfolk can breathe air and water."
    obj.speed["ground"] = 10
    obj.speed["swim"] = 40
    obj.languages.append("Aquan")

def orc(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(orc)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[3] -= 2 # -2 to Int
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Aggressive"] = "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see."
    obj.senses["darkvision"] = 60
    obj.languages.append("Orc")

def skeleton(obj):
    obj.type = "undead"
    obj.race = None
    obj.abilities[1] += 2 # +2 to Dex
    obj.abilities[3] -= 4 # -4 to Int
    obj.abilities[5] -= 4 # -4 to Cha
    obj.update_modifiers()
    obj.update_perception()
    obj.senses["darkvision"] = 60
    obj.languages = ["understands all languages it knew in life but can't speak"]
    obj.vulnerable ["bludgeoning"]
    obj.dmg_immune = ["poision"]
    obj.cond_immune = ["exhausted", "poisoned"]

def tiefling(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(tiefling)"
    obj.abilities[3] += 1 # +1 to Int
    obj.abilities[5] += 2 # +2 to Cha
    obj.update_modifiers()
    obj.update_perception()
    if obj.cr < 3:
        obj.features["Infernal Legacy"] = "The tiefling knows the <i>thaumaturgy</i> cantrip. Charisma is the casting modifier for this spell."
    elif obj.cr >= 3 and obj.cr < 5:
        obj.features["Infernal Legacy"] = "The tiefling knows the <i>thaumaturgy</i> cantrip, and can cast <i>hellish rebuke</i> as a 2nd-level spell once per long rest. Charisma is the casting modifier for this spell."
    else:
        obj.features["Infernal Legacy"] = "The tiefling knows the <i>thaumaturgy</i> cantrip, <i>hellish rebuke</i> as a 2nd-level spell once per long rest, and they can cast <i>darkness</i> once per long rest. Charisma is the casting modifier for this spell."
    obj.dmg_resist = ["fire"]
    obj.senses["darkvision"] = 60
    obj.languages.append("Infernal")

def troglodyte(obj):
    obj.size = "Medium"
    obj.type = "humanoid"
    obj.race = "(troglodyte)"
    obj.abilities[0] += 2 # +2 to Str
    obj.abilities[2] += 2 # +2 to Con
    obj.abilities[3] -= 4 # -4 to Int
    obj.abilities[5] -= 4 # -4 to Cha
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Chameleon Skin"] = "The troglodyte has advantage on Dexterity (stealth) checks made to hide."
    obj.features["Stench"] = "Any creature other than a troglodyte that starts its turn within 5 feet of the troglodyte must succeed a DC 12 Constitution saving throw of be poisoned until the start of the creature's next turn. On a successful saving throw, the creature is immune to the stench of all troglodytes for 1 hour."
    obj.features["Sunlight Sensitivity"] = "While in the sunlight, the troglodyte has disadvantage on attack rolls, as well as Wisdom (Perception) checks that rely on sight."
    obj.armor += 1
    obj.senses["darkvision"] = 60
    obj.languages.append("Troglodyte")

def zombie(obj):
    obj.type = "undead"
    obj.race = None
    obj.abilities[0] += 1 # +1 to Str
    obj.abilities[2] += 2 # +2 to Con
    obj.abilities[3] -= 6 # -6 to Int
    obj.abilities[4] -= 4 # -4 to Wis
    obj.abilities[5] -= 4 # -4 to Cha
    obj.update_modifiers()
    obj.update_perception()
    obj.features["Undead Fortitude"] = "If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie drops to 1 hit point instead."
    obj.senses["darkvision"] = 60
    obj.languages = ["understands all languages it knew in life but can't speak"]
    obj.vulnerable ["bludgeoning"]
    obj.dmg_immune = ["poision"]
    obj.cond_immune = ["poisoned"]
