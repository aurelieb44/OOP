#actually creating a coin

import CoinClass as c #using an alias c
# Importing the .py that is the object definition file. 
# I'm not importing the name of the file but the name of the file.

# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   
       # this creates an instance called 'my_coin' of the class 'Coin()'
       # my_coin is a instance/object of the coin class
       # All the methods are available to you at the instance
       # You wouldn't use Coin naymore, but my_coin.

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    
       # notice you do not have to supply the argument/parameter
       # when we create a new instance, the value is set to head by default.

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

# Call the main function.

main()
