class BankAccount:

    num_of_accounts = 0
    all_acct_instances = []

    def __init__(self, interest_rate = .02,balance = 0):
        self.interest_rate = interest_rate
        self.balance = balance
        print(f"Account Initiated. Interest rate: {self.interest_rate}. Balance: ${self.balance}.")
        BankAccount.all_acct_instances.append(self)
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit amount: ${amount}. New balance: ${self.balance}")
        return self
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Withdrawal amount: ${amount}")
            return self
        else:
            print(f"You tried to withdraw ${amount} when your balance was ${self.balance} = Insufficient funds: Charging a $5 fee.")
            self.balance -= 5.0
            return self
    def display_account_info(self):
        print(f"ACCOUNT INFO\n-------------\nInterest rate: {self.interest_rate}. Balance: ${self.balance}.")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
            print(f"Interest rate generated increased of: ${self.balance * self.interest_rate}")
            return self
        else:
            print(f"No increase possible.")
    @classmethod
    def get_each_instances_info(cls):
        print(f"EACH INSTANCE AND ITS INFO: ")
        for checking in cls.all_acct_instances:
            BankAccount.display_account_info(checking) # hard coding which child account temporarily until successful testing of inheritance.
        print("\n")



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate = 0.2, balance = 0)
    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_with_account_info(self):
        print(f"{self.name}'s account info:")
        self.account.display_account_info()
        return self

# TEST:
user01 = User("Captain Jean-Luc Picard","JLPicard@starfleet.earth")
user01.deposit(200).display_user_with_account_info().withdraw(250)

user02 = User("Sancho Pancakes", "dons.sidekick@wild.times")
user02.withdraw(5).display_user_with_account_info()