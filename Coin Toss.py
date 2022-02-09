#actually creating a coin

import CoinClass as c #using an alias c
# Importing the .py that is the object definition file. 
# I'm importing the .py file, that is the object definition file. 
# I'm not importing the name of the class, I'm importing the name of the file.

# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   
       # this creates an instance called 'my_coin' of the class 'Coin()'
       # my_coin is a instance/object that belongs to the coin class. 
       # Just like name is an object that belongs to the string class.
       # All the methods are available to you at the instance.
       # You wouldn't use Coin anymore, but my_coin.

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    
       # notice you do not have to supply the argument/parameter
       # when we create a new instance, when we first initialize, automatically the value is set to 'heads' by default.

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           # call the toss method of my instance which belongs to my class.
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())
           # We are not manipulating the sideup attribute directly. 
           # We are calling the method toss that allows us to flip it and then we can print out the value.

# Call the main function.
main()
