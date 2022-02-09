import CellPhoneClass as c

my_phone = c.CellPhone('Xiaomi','YUUO','200')

def main():
    
    #my_phone.set_manufact()
    #my_phone.set_model()
    #my_phone.set_retail_price()

    #display
    print('Phone Manufacturer: ', my_phone.get_manufact())
    print('Phone Model Number: ', my_phone.get_model())
    print('Phone Retail Price: ', my_phone.get_retail_price())

main()