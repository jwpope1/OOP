import random


class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0
        dist = 0
        self.insect = "House Fly"

    def bug_type(self):
        if random.randint(0, 1) == 0:
            self.insect = "House Fly"
        else:
            self.insect = "Mosquito"

    def length_of_flight(self):
        self.flight = random.randint(1, 10)

    def get_flight(self):
        return self.insect
        return self.flight
