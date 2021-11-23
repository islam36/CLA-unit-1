class Rectange:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Vehicule:
    def __init__(self, max_speed, millage):
        self.max_speed = max_speed
        self.millage = millage

class vehicule:
    pass

class Bus(Vehicule):
    def __init__(self, max_speed, millage):
        super().__init__(max_speed, millage)