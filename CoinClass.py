#The class definition file
#The blueprint of how to create an object/coin

import random

# The Coin class simulates a coin that can
# be flipped.

class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):
        self.__sideup = 'Heads' 
        #adding two underscores will hide our data attributes
        #have to do it everywhere, it's not the same attribute anymore

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.
    # we don't want the user to change the value of sideup. 
    # we only allow the user to change the value through toss.

    def toss(self):
        if random.randint(0, 1) == 0: #randomly picks 0 or 1
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
            return self.__sideup
    #returns the value of our attribute called sideup.
