# Create Pokemon Class

class Pokemon:

    def __init__(self, name, level, type_):


        self.name = name
        self.level = level
        self.type = type_
        self.max_health = level
        self.current_health = level
        self.knocked_out = False

    def knock_out(self):

        if self.knocked_out == False:

            self.knocked_out = True

            print("{name} was knocked out!".format(name = self.name))

        else:
            raise ValueError
        
    def loose_health(self, value):

        if value <= 0 or not isinstance(value, int):
            raise ValueError
        
        elif value < self.current_health:
            self.current_health -= value

            if value == 1:
                print("{name} lost 1 health point!".format(name = self.name))

            else:
                print("{name} lost {value} health points!".format(name = self.name, value = value))

        else:
            print("{name} lost {value} health points!".format(name = self.name, value = self.current_health))
            self.current_health = 0
            self.knock_out()

    def revive(self):
        if self.knocked_out == True:

            self.current_health = int(self.max_health * 0.3)
            self.knocked_out = False

            print("{name} was revived and now has {value} health points.".format(name = self.name, value = self.current_health))

        else:
            print("{name} is not knocked out and cannot be revived.".format(name = self.name))



    def heal(self, value):

        if value <= 0 or not isinstance(value, int):

            raise ValueError

        elif self.knocked_out == True:
            print("{name} is knocked out and cannot be healed.".format(name = self.name))



        elif self.current_health == self.max_health:

            print("{name} is at full health and cannot be healed.".format(name = self.name))

    
        elif self.current_health + value > self.max_health:

            gained_health = self.max_health - self.current_health

            self.current_health = self.max_health


            if gained_health > 1:
                print("{name} gained {gained_health} health points!.".format(name = self.name, gained_health = gained_health))

            else:
                print("{name} gained 1 health point!.".format(name = self.name))

            

        else:
            self.current_health += value

            if value >1:
                print("{name} gained {gained_health} health points!.".format(name = self.name, gained_health = value))

            else:
                print("{name} gained 1 health point!.".format(name = self.name))



    def attack(self, value, opponent):

        if isinstance(opponent, Pokemon) and opponent != self:

            print("{self} attacked {opponent}!".format(self = self.name, opponent = opponent.name))



            if self.type.check_effektive(opponent.type) == True:
                damage = value * 2

                print("The attack was effektive!")

            elif self.type.check_weak_against(opponent.type) == True:
                damage = int(value/2) 

                print("The attack wasn't effektive.")


            else:
                damage = value

              

            opponent.loose_health(damage)

        else:
            raise ValueError


class Element:

    def __init__(self, name, effektive_against = [], weak_against = []):
        
        self.name = name
        self.effektive_against = effektive_against
        self.weak_against = weak_against
        
    def __str__(self):
        return self.name

    def __repr__(self):

        string_effektive = [str(element) for element in self.effektive_against]
        string_weak = [str(element) for element in self.weak_against]
        
        return "Name: {type_}, effektive against: {effektive_list}, weak against: {weak_list}".format(type_ = self.name, effektive_list = string_effektive, weak_list = string_weak)

    def add_effektive(self, type_):
        self.effektive_against.append(type_)

    def add_weak_against(self, type_):
        self.weak_against.append(type_)

    def check_effektive(self, other):

        if other in self.effektive_against:
            return True

        else:
            return False

    def check_weak_against(self, other):
        if other in self.weak_against:
            return True
        else:
            return False
        
# Creating elements

water = Element("Water")

fire = Element("Fire", [], [water])

grass = Element("Grass", [water], [fire])

fire.add_effektive(grass)

water.add_effektive(fire)
water.add_weak_against(grass)


pokA = Pokemon("A", 100, water)
pokB = Pokemon("B", 100, fire)
pokC = Pokemon("C", 100, fire)

pokB.attack(20, pokC)

pokA.attack(40, pokC)







