import npc

walter = npc.NPC("Walter")

#Checking the name methods
print(walter.get_name()) #works
#alter it and print it
walter.set_name("Walt")
print(walter.get_name())

#Checking the challenge rating and associated proficiency
print(walter.get_rating()) #works
print(walter.get_proficiency()) #works
#alter it then print it
walter.set_challenge_rating(12) #works
print(walter.get_rating())
print(walter.get_proficiency())
#should fail
walter.set_challenge_rating(-2) #good!
print(walter.get_rating())
print(walter.get_proficiency())

#Check size methods
print(walter.get_size()) #works

walter.set_size("Small") #works
print(walter.get_size())

walter.set_size("Big") #should fail
print(walter.get_size()) #good

#Type methods
print(walter.get_type()) #good

walter.set_type("fey") #good
print(walter.get_type())

walter.set_type("orc") #should fail
print(walter.get_type()) #good

#Race methods
print(walter.get_race()) #works

#Alignment methods
print(walter.get_alignment())

walter.set_alignment("lawful neutral")
print(walter.get_alignment()) #good

walter.set_alignment("chaotic stupid") #should fail
print(walter.get_alignment()) #good

#Ability score testing
print(walter.get_ability_score("CON")) #good
print(walter.get_modifier("CON")) #good
#HP
print(walter.get_hp()) #good
walter.set_challenge_rating(1) #good
walter.set_hp() #good
print(walter.get_hp()) #good

walter.update_dicecode()
print(walter.get_dicecode())
