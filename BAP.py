import BAC as bac

my_bal = bac.BankAccount(int(input('whats your balance? ')))


depo = int(input('how much to deposit? '))
my_bal.deposit(depo)

withdrawal = int(input('how much to withdraw? '))
my_bal.withdraw(withdrawal)

print(my_bal.get_bal())
