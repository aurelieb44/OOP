import CarClass as c

my_car = c.Car(2020, 'Toyota')

def main():
    print('I am going to accelerate 5 times:')
    for count in range (5):
        my_car.accelerate()
        print('The current speed is: ', my_car.get_speed())

    print('I am going to brake 5 times:')  
    for count in range(5):
        my_car.brake()
        print('The current speed is: ', my_car.get_speed())

main()