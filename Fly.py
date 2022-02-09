import InsectClass as i 



def main():
    #it won't create an instance unless you supply 2 values
    fly = i.Insect(2,4)    #create an instance

    fly.flight_length()

    print('The insect can fly up to ', fly.get_miles(), 'miles')

main()
