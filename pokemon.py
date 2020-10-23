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

        self.knocked_out = True
        
    def loose_health(self, value):

        if value < self.current_health:
            self.current_health -= value

        else:
            self.current_health = 0
            self.knock_out()


        

        

test = Pokemon("charizard", 50, "fire")

test.loose_health(10)

print(test.current_health)

test.loose_health(40)

print(test.current_health)
print(test.knocked_out)




