import CellPhoneClass as c

my_phone = c.CellPhone('Xiaomi','YUUO','200')

def main():
    #display
    print('Phone Manufacturer: ', my_phone.get_manufact())
    print('Phone Model Number: ', my_phone.get_model())
    print('Phone Retail Price: ', my_phone.get_retail_price())

    #print(my_phone)

main()