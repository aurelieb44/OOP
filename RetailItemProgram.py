import RetailItemClass as r 
    
def main():

    item1 = r.RetailItem('Jacket', 12, 59.95)

    item2 = r.RetailItem('Designer Jeans', 40, 34.95)

    item3 = r.RetailItem('Shirt', 20, 24.95)

    print('Item Number\t Description\t\t Units in Inventory\t Price')
    print('Item #1: \t', item1.get_desc(),'\t\t', item1.get_inventory(), '\t\t\t', item1.get_price())
    print('Item #2: \t', item2.get_desc(),'\t', item2.get_inventory(), '\t\t\t', item2.get_price())
    print('Item #3: \t', item3.get_desc(),'\t\t\t', item3.get_inventory(), '\t\t\t', item3.get_price())

main()