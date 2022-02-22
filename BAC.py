class BankAccount:

    def __init__(self,bal):
        self.__bal = bal
    
    def deposit(self,cash):
        self.__bal += cash
    
    def withdraw(self,cash):
        if cash <= 0:
            print('fool')
        else:
            self.__bal -= cash

    def get_bal(self):
        return self.__bal 