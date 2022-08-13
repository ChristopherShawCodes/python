# Looking at the following we would usually write our code out as 2 seperate classes


# class CheckingAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#     def deposit(self, amount):
#     	# code
#     def withdraw(self, amount):
#     	# code
#     def write_check(self, amount):
#     	# code
#     def display_account_info(self):
#     	# code

#         class RetirementAccount:
#     def __init__(self, int_rate, is_roth, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#     	self.is_roth = is_roth
#     def deposit(self, amount):
#     	# code - assess tax if necessary
#     def withdraw(self, amount):
#     	# code - assess penalty if necessary
#     def display_account_info(self):
#     	# code




# Super
# Here's what we want our RetirementAccount __init__ method to do,
#  and what our parent BankAccount class __init__ method does:

# class RetirementAccount(BankAccount):
#     def __init__(self, int_rate, is_roth, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#     	self.is_roth = is_roth  
# copy
# class BankAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance

# Do you see how the parent class already does 2 of the 3 lines we're 
# trying to execute in our RetirementAccount class? LINES 38,39,44,45
#  Let's utilize the parent's functionality for this method.
#  To indicate we are trying to use the parent's methods,
#  we call on it with the keyword super. 
# From there, we can call on any of the parent's methods:

# class RetirementAccount(BankAccount):
#     def __init__(self, int_rate, is_roth, balance=0):
#     	super().__init__(int_rate, balance)	
#         self.is_roth = is_roth	

# class BankAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance


# The first line in our RetirementAccount __init__ method allows the parent
#  to manage the setting of int_rate and balance. 
#  The only line we need to add is to set the is_roth attribute, 
#  since this is unique to the RetirementAccount class.
