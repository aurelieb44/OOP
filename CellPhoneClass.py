class CellPhone:

    def __init__(self, manu, modelno, price):
        self.__manufact = manu
        self.__model = modelno
        self.__retail_price = price

    def set_manufact(self, manu):
        self.__manufact = manu

    def set_model(self, modelno):
        self.__model = modelno

    def set_retail_price(self, price):
        self.__retail_price = price

    def get_manufact(self): 
        return self.__manufact

    def get_model(self): 
        return self.__model

    def get_retail_price(self): 
        return self.__retail_price

    #def __str__(self):
        #return self.__manufact