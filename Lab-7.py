class ATM:
    def __init__(self,acc_holder,balance=0):
        self.acc_holder=acc_holder
        self.balance=balance
    def check_balance(self):
        return f"{self.acc_holder}, Your current balance is:{self.balance:.2f}"
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f"{self.acc_holder}, You deposited {amount:.2f}\nYour current balance is {self.balance:.2f}"
        else:
            return "transaction failed. Enter amount greater than zero"
    def withdrawal(self,amount):
        if amount>self.balance:
            return "Withdrawal failed. Insufficient funds"
        elif amount<=0:
            return "Enter amount greater than zero"
        else:
            self.balance-=amount
            return f"{self.acc_holder}, You withdrew {amount:.2f}\nYour current balance is {self.balance:.2f}"
    def transfer(self,other_acc,amount):
        if amount>self.balance:
            return f"{self.acc_holder}, You have insufficient funds for transfer."
        else:
            self.balance-=amount
            other_acc.balance+=amount
            return f"The amount {amount} has been tranferred from account under {self.acc_holder} to account under {other_acc.acc_holder}"
my_acc=ATM(acc_holder="Anna",balance=1000)
other_acc=ATM(acc_holder="Jenny",balance=300)
print(my_acc.check_balance)
print(my_acc.deposit(400))
print(my_acc.withdrawal(200))
print(my_acc.transfer(other_acc,500))
