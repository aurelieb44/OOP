import random

class Insect:

    def __init__(self,w,l): 
        #self.legs = 4 #hardcoded numbers
        #self.wings = 2
        self.legs = w #additional parameters
        self.wings = l
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1, 10)

    def get_miles(self): #accessor method
        # we want a separate accessor method for each attribute
        return self.flight

