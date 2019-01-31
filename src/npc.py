class NPC:
    def __init__(self, name):
        self.name = str(name)
        self.cr = 0
        self.size = "Medium"
        self.type = "humanoid"
        self.race = "(human)"
        self.alignment = "neutral"
        self.abilities = [10,10,10,10,10,10]
        self.modifiers = [0,0,0,0,0,0]
        self.proficiency = 2
        self.armor = 10
        self.hp = 1
        self.dicecode = "(1d6)"
        self.features = {}
        self.actions = {}
        self.items = {}
        self.spells = []

    #Accessor methods
    def get_name(self):
        return str(self.name)

    def get_rating(self):
        return self.cr

    def get_size(self):
        return str(self.size)

    def get_type(self):
        return str(self.type)

    def get_race(self):
        return str(self.race)

    def get_alignment(self):
        return str(self.race)

    def get_ability_score(self, ability):
        ability = str(ability)
        if ability == "STR":
            score = self.abilities[0]
        elif ability == "DEX":
            score = self.abilities[1]
        elif ability == "CON":
            score = self.abilities[2]
        elif ability == "INT":
            score = self.abilities[3]
        elif ability == "WIS":
            score = self.abilities[4]
        elif ability == "CHA":
            score = self.abilities[5]
        else:
            print("INPUT ERROR: Not a recognized ability tag!")
            return None
        return str(score)

    def get_modifier(self, ability):
        ability = str(ability)
        if ability == "STR":
            modifier = self.modifiers[0]
        elif ability == "DEX":
            modifier = self.modifiers[1]
        elif ability == "CON":
            modifier = self.modifiers[2]
        elif ability == "INT":
            modifier = self.modifiers[3]
        elif ability == "WIS":
            modifier = self.modifiers[4]
        elif ability == "CHA":
            modifier = self.modifiers[5]
        else:
            print("INPUT ERROR: Not a recognized ability tag!")
            return None
        return str(modifier)

    def get_proficiency(self):
        return self.proficiency

    def get_armor(self):
        return self.armor

    def get_hp(self):
        return self.hp

    def get_dicecode(self):
        return self.dicecode

    def get_feature(self, feature):
        feature = str(feature)
        return self.features[feature]

    def get_action(self, action):
        action = str(action)
        return self.actions[action]

    def get_item(self, item):
        item = str(item)
        return self.items[item]

    #Mutator methods
    def set_name(self, name):
        self.name = str(name)

    def set_size(self, size):
        size = str(size)
        #FIXME: There has got to be a better way to check these.
        if size == "Tiny":
            self.size = size
        elif size == "Small":
            self.size = size
        elif size == "Medium":
            self.size = size
        elif size == "Large":
            self.size = size
        elif self.size == "Huge":
            self.size = size
        elif self.size == "Gargantuan":
            self.size == size
        else:
            print("INPUT ERROR: Please choose an appropriate size!")

    def set_type(self, type):
        type = str(type)
        if type == "aberration":
            self.type = type
        elif type == "beast":
            self.type = type
        elif type == "celestial":
            self.type = type
        elif type == "construct":
            self.type = type
        elif type == "dragon":
            self.type = type
        elif type == "elemental":
            self.type = type
        elif type == "fey":
            self.type = type
        elif type == "fiend":
            self.type = type
        elif type == "giant":
            self.type = type
        elif type == "humanoid":
            self.type = type
        elif type == "monstrosity":
            self.type = type
        elif type =="ooze":
            self.type = type
        elif type == "plant":
            self.type = type
        elif type == "undead":
            self.type = type
        else:
            print("INPUT ERROR: Please choose an appropriate type!")
            print("(N.B.: Make sure it is lowercase.)")

    def set_alignment(self, alignment):
        alignment = str(alignment)
        if alignment == "lawful good":
            self.alignment = alignment
        elif alignment == "neutral good":
            self.alignment = alignment
        elif alignment == "chaotic good":
            self.alignment = alignment
        elif alignment == "lawful neutral":
            self.alignment = alignment
        elif alignment == "neutral":
            self.alignment = alignment
        elif alignment == "chaotic neutral":
            self.alignment = alignment
        elif alignment == "lawful evil":
            self.alignment = alignment
        elif alignment == "neutral evil":
            self.alignment = alignment
        elif alignment == "chaotic evil":
            self.alignment = alignment
        elif alignment == "unaligned":
            self.alignment = alignment
        else:
            print("INPUT ERROR: Please choose a valid alignment!")
            print("(N.B.: Make sure it is lowercase.)")

    def set_ability_score(self, ability, score):
        ability = str(ability)
        score = int(score)
        if score <= 30 and score > 0:
            if ability == "STR":
                self.abilities[0] = score
            elif ability == "DEX":
                self.abilities[1] = score
            elif ability == "CON":
                self.abilities[2] = score
            elif ability == "INT":
                self.abilities[3] = score
            elif ability == "WIS":
                self.abilities[4] = score
            elif ability == "CHA":
                self.abilities[5] = score
            else:
                print("INPUT ERROR: Not a recognized ability tag!")
        else:
            print("INPUT ERROR: Invalid score range!")
            print("Please choose a value between 1 and 30.")

    def update_modifiers(self):
        for index, modifer in enumerate(self.modifiers):
            modifer = (self.abilities[index] - 10)//2

    def set_challenge_rating(self, cr):
        cr = float(cr)
        if cr >= 0:
            self.cr = cr
        else:
            print("INPUT ERROR: Please select a valid CR!")
            return None

        if cr >= 0 and cr <= 4:
            self.proficiency = 2
        elif cr > 4 and cr <= 8:
            self.proficiency = 3
        elif cr > 8 and cr <= 12:
            self.proficency = 4
        elif cr > 12 and cr <= 16:
            self.proficency = 5
        elif cr > 16 and cr <= 20:
            self.proficency = 6
        elif cr > 20 and cr <= 24:
            self.proficency = 7
        elif cr > 24 and cr <= 28:
            self.proficency = 8
        else:
            self.proficency = 9
