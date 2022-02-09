# The BankAccount class simulates a bank account.

class BankAccount:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute. only one attribute, that is coming in from the user.

    def __init__(self, bal):
        self.__balance = bal

      # The deposit method makes a deposit into the
      # account.

    def deposit(self, amount): # mutator method
        self.__balance += amount

      # The withdraw method withdraws an amount
      # from the account.

    def withdraw(self, amount):
      if amount <= 0: #to make sure the user doesn't withdraw a negative amount
        print('You Fool!')
      else:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

      # The get_balance method returns the
      # account balance.

    def get_balance(self): #accessor method
        return self.__balance
        # we don't need arguments in that. 
        # The mutator method requires additional argument.

    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')
