import InsectClass as i 

def main():
       my_insect = i.Insect()   

       print('The flight is: ', my_insect.get_flight(), ' miles')    

       print('I am going to do it ten times:')
       for count in range(10):
           my_insect.flight()

           print('The flight is: ', my_insect.get_flight(), ' miles')  


main()
