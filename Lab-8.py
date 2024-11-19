class Account:
    def __init__(self, acc_no, acc_holder, balance=0):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.balance = balance
        self.transaction_history = TransactionHistory()

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.add_transaction("Deposit", amount)
            print(f"Deposit of {amount} successful. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            self.transaction_history.add_transaction("Withdrawal", amount)
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")

class SavingAccount(Account):
    def __init__(self, acc_no, acc_holder, balance=0, withdrawal_limit=5000):
        super().__init__(acc_no, acc_holder, balance)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Amount exceeds withdrawal limit of {self.withdrawal_limit}.")
        else:
            super().withdraw(amount)

class CurrentAccount(Account):
    def __init__(self, acc_no, acc_holder, balance=0, overdraft_limit=2000):
        super().__init__(acc_no, acc_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > (self.balance + self.overdraft_limit):
            print("Amount exceeds overdraft limit.")
        else:
            self.balance -= amount
            self.transaction_history.add_transaction("Withdrawal", amount)
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")

class CheckingAccount(Account):
    def __init__(self, acc_no, acc_holder, balance=0, withdrawal_limit=10000):
        super().__init__(acc_no, acc_holder, balance)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Amount exceeds withdrawal limit of {self.withdrawal_limit}.")
        else:
            super().withdraw(amount)

class TransactionHistory:
    def __init__(self):
        self.history = []

    def add_transaction(self, transaction_type, amount):
        self.history.append({"type": transaction_type, "amount": amount})

    def show_history(self):
        if not self.history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for record in self.history:
                print(f"{record['type']}: {record['amount']}")

# Example Usage:
saving_acc = SavingAccount(acc_no=12345, acc_holder="Alice", balance=10000, withdrawal_limit=3000)
saving_acc.deposit(2000)
saving_acc.withdraw(2500)
saving_acc.withdraw(5000)
saving_acc.transaction_history.show_history()

current_acc = CurrentAccount(acc_no=67890, acc_holder="Bob", balance=5000)
current_acc.withdraw(6000)  # Within overdraft limit
current_acc.withdraw(8000)  # Exceeds overdraft limit
current_acc.transaction_history.show_history()

checking_acc = CheckingAccount(acc_no=11223, acc_holder="Charlie", balance=7000, withdrawal_limit=5000)
checking_acc.withdraw(6000)  # Exceeds withdrawal limit
checking_acc.withdraw(4000)  # Within withdrawal limit
checking_acc.transaction_history.show_history()
