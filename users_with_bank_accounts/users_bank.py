class user:
    def __init__(self,first_name, last_name, email, age, balance, int_rate):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = BankAccount(balance,int_rate)
# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def user_deposit(self):
        self.account.deposit()

# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.

    def user_withdrawal(self):
        self.account.withdraw()

# Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self):
        self.account.display_account_info()

class BankAccount:
    all_accounts = []

    def __init__(self,balance=0,int_rate=0.01):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance = self.balance
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate + self.balance
        return self

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        print(sum)
        return(sum)

    @classmethod
    def all_account_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()

numeroUno = user("Christopher","Shaw","admin@thejitteryape.io","33","168000","0.1")
numeroUno.display_user_balance()  