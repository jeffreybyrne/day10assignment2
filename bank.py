# Create a BankAccount class
# Every bank account should have balance and interest_rate attributes (instance variables)
# Since we want these fields to be set for every account, you'll need to add an __init__ method to your class

# There should be a withdraw instance method that accepts one amount argument and subtracts it from the total balance
# Don't forget to test it out!
# Finally, there should be a gain_interest instance method that increases the total balance according to the interest rate.

class BankAccount:

    def __init__(self,balance=0,interest_rate=0):
        self.balance = balance
        self.interest_rate = interest_rate

# Define a __str__() instance method so you can print bank account objects and see a nice, meaningful string. Make sure this method returns a string,
# rather than printing it!
    def __str__(self):
        return "The current balance is {} with an interest rate of {}%".format(self.balance,self.interest_rate)

# Your class should have an instance method called deposit that accepts one amount argument and adds that amount to the total balance
# Test out your method by calling it on an instance of your class


# At this point you should test out creating an instance of your class to make sure it works
my_bank = BankAccount(40,7)
print(my_bank)
