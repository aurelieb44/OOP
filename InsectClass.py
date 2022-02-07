import random

class Insect:

    def __init__(self):
        self.legs = 4
        self.wings = 2
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1, 10)

    def get_flight(self):
        return self.flight

