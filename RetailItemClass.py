from pydoc import describe


class RetailItem:

    def __init__(self, desc, inventory, price):
        self.__desc = desc
        self.__inventory = inventory
        self.__price = price
    
    def set_desc(self, desc):
        self.__desc = desc
    
    def set_inventory(self, inventory):
        self.__inventory = inventory
    
    def set_desc(self, price):
        self.__price = price
    
    def get_desc(self):
        return self.__desc

    def get_inventory(self):
        return self.__inventory

    def get_price(self):
        return self.__price