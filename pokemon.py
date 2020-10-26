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




        

        

test = Pokemon("charizard", 50, "fire")

test.loose_health(80)

test.heal(40)

test.revive()
print(test.knocked_out)

print(test.current_health)
