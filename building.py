import random

class Building(object):
    type
    details

    def __init__(self):
        self.type = ''
        self.details = ''

        # Roll the building's type
        roll = random.randint(1,20)

        if roll <= 10:
            self.type = "Residence"

            # Roll details for residences
            roll = random.randint(1 20);
            if roll <= 2
                self.details = "Abandoned Squat"
            elif roll > 2 && roll <= 8
                self.details = "Middle-class home"
            elif roll > 8 && roll <= 10
                self.details = "Upper-class home"
            elif roll > 10 && roll <= 15
                self.details = "Crowded tenement"
            elif roll > 15 && roll <= 17
                self.details = "Orphanage"
            elif roll == 18
                self.details = "Hidden slaver's den"
            elif roll == 19
                self.details = "Front for a secret cult"
            else
                self.details = "Lavish, guarded mansion"

        # Religious building
        elif roll > 10 && roll <= 12
            self.type = "Religious building"

            # Roll details for religious buildings
            roll = random.randint(1, 20)
            if roll <= 10
                self.details = "Temple to a good or neutral deity"
            elif roll > 10 && roll <= 12
                self.details = "Temple to a false deity (run by charlatan priests"
            elif roll == 13
                self.details = "Home of ascetics"
            elif roll > 13 && roll <= 15
                self.details = "Abandeoned shrine"
            elif roll > 15 && roll <= 17
                self.details = "Library dedicated to religious study"
            else
                self.details = "Hidden shrine to a fiend or evil deity"

            # Tavern
        elif roll > 12 && roll <=15
            # Create Tavern Name
            firstpart = ""
            secondpart = ""

            roll = random.randint(1, 20)
            if roll == 1
                firstpart = "The Silver"
            elif roll == 2
                firstpart = "The Golden"
            elif roll == 3
                firstpart = "The Staggering"
            elif roll == 4
                firstpart = "The Laughing"
            elif roll == 5
                firstpart = "The Prancing"
            elif roll == 6
                firstpart = "The Gilded"
            elif roll == 7
                firstpart = "The Running"
            elif roll == 8
                firstpart = "The Howling"
            elif roll == 9
                firstpart = "The Slaughtered"
            elif roll == 10
                firstpart = "The Leering"
            elif roll == 11
                firstpart = "The Drunken"
            elif roll == 12
                firstpart = "The Leaping"
            elif roll == 13
                firstpart = "The Roaring"
            elif roll == 14
                firstpart = "The Frowning"
            elif roll == 15
                firstpart = "The Lonely"
            elif roll == 16
                firstpart = "The Wandering"
            elif roll == 17
                firstpart = "The Mysterious"
            elif roll == 18
                firstpart = "The Barking"
            elif roll == 19
                firstpart = "The Black"
            else
                firstpart = "The Gleaming"

            roll = random.randint(1, 20)
                if roll == 1
                    secondpart = "Eel";
                elseif roll == 2
                    secondpart = "Dolphin";
                elseif roll == 3
                    secondpart = "Dwarf";
                elseif roll == 4
                    secondpart = "Pegasus";
                elseif roll == 5
                    secondpart = "Pony";
                elseif roll == 6
                    secondpart = "Rose";
                elseif roll == 7
                    secondpart = "Stag";
                elseif roll == 8
                    secondpart = "Wolf";
                elseif roll == 9
                    secondpart = "Lamb";
                elseif roll == 10
                    secondpart = "Demon";
                elseif roll == 11
                    secondpart = "Goat";
                elseif roll == 12
                    secondpart = "Spirit";
                elseif roll == 13
                    secondpart = "Horde";
                elseif roll == 14
                    secondpart = "Jester";
                elseif roll == 15
                    secondpart = "Mountain";
                elseif roll == 16
                    secondpart = "Eagle";
                elseif roll == 17
                    secondpart = "Satyr";
                elseif roll == 18
                    secondpart = "Dog";
                elseif roll == 19
                    secondpart = "Spider";
                else
                    secondpart = "Star";
                end

                tavernname = firstpart + " " + secondpart;
                building.type = "Tavern: " + tavernname;

                % Roll details for taverns
                roll = randi([1, 20]);
                if roll < 5
                    building.details = "Quiet, low-key bar";
                elseif roll > 5 && roll <= 9
                    building.details = "Raucous dive";
                elseif roll == 10
                    building.details = "Thieves' guild hangout";
                elseif roll == 11
                    building.details = "Gathering place for a secret society";
                elseif roll > 11 && roll <= 13
                    building.details = "Upper-class dining club";
                elseif roll > 13 && roll <= 15
                    building.details = "Gambling den";
                elseif roll > 15 && roll <= 17
                    building.details = "Caters to specific race or guild";
                elseif roll == 18
                    building.details = "Members-only club";
                else
                    building.details = "Brothel";
                end

            %Warehouses
            elseif roll > 15 && roll <= 17
                %building = Building();      % Remove if not playing CoS

                %---- UNCOMMENT IF NOT PLAYING COS ----%
                building.type = "Warehouse";

                % Roll dtails for warehouses
                roll = randi([1, 20]);
                if roll < 4
                    building.details = "Empty or abandoned";
                elseif roll > 4 && roll <= 6
                    building.details = "Heavily guarded, expensive goods";
                elseif roll > 6 && roll <= 10
                    building.details = "Cheap goods";
                elseif roll > 10 && roll <= 14
                    building.details = "Bulk goods";
                elseif roll == 15
                    building.details = "Live animals";
                elseif roll > 15 && roll <= 17
                    building.details = "Weapons/armor";
                elseif roll > 17 && roll <= 19
                    building.details = "Goods from a distant land";
                else
                    building.details = "Secret smuggler's den";
                end

            % Shops
            else
                %building = Building();      %Remove if not playing CoS

                 %---- UNCOMMENT IF NOT PLAYING COS ----%
                building.type = "Shop";

                % Roll details for shops
                roll = randi([1, 20]);
                if roll == 1
                    building.details = "Pawnshop";
                elseif roll == 2
                    building.details = "Herbs/incense";
                elseif roll == 3
                    building.details = "Fruits/vegetables";
                elseif roll == 4
                    building.details = "Dried meats";
                elseif roll == 5
                    building.details = "Pottery";
                elseif roll == 6
                    building.details = "Undertaker";
                elseif roll == 7
                    building.details = "Books";
                elseif roll == 8
                    building.details = "Moneylender";
                elseif roll == 9
                    building.details = "Weapons/armor";
                elseif roll == 10
                    building.details = "Chandler";
                elseif roll == 11
                    building.details = "Smithy";
                elseif roll == 12
                    building.details = "Carpenter";
                elseif roll == 13
                    building.details = "Weaver";
                elseif roll == 14
                    building.details = "Jeweler";
                elseif roll == 15
                    building.details = "Baker";
                elseif roll == 16
                    building.details = "Mapmaker";
                elseif roll == 17
                    building.details = "Tailor";
                elseif roll == 18
                    building.details = "Ropemaker";
                elseif roll == 18
                    building.details = "Mason";
                else
                    building.details = "Scribe";
                end
            end
        end

    end
end
