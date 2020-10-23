# Create Pokemon Class

class Pokemon:

    def __init__(self, name, level, type_):


        self.name = name
        self.level = level
        self.type = type_
        self.max_health = level
        self.current_health = level
        self.knocked_out = False


test = Pokemon("charizard", 50, "fire")
