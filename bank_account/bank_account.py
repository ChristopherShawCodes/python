class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print(f"Account Balance: {self.balance}")
        print(f"Interest Rate: {self.int_rate}")
        return self
    def yield_interest(self):
        self.int_rate += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

user_one = BankAccount(1000039.41,1)
user_two = BankAccount(849888.12,3)

user_one.deposit(447.60).deposit(12.01).deposit(845.91).withdraw(45.00)
user_two.deposit(13.99).deposit(27.42).withdraw(12.83).withdraw(12.83).withdraw(12.83).withdraw(12.83).yield_interest().display_account_info()

BankAccount.print_all_accounts()