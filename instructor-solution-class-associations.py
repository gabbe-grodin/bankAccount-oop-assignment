class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0) # calling the BankAccount class creates an instance for the User

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self
    
    # def display_account_info(self):
    #     pass
    
class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: You will be charged a $5.00 fee.")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
@classmethod
def print_all_accounts(cls):
    for account in cls.accounts:
        account.display_account_info()

# User Test:

user1 = User("Clairy Cherry", "clair.owens@dogs.moredogs")
user1.make_deposit(36).make_deposit(218).display_user_balance()

user2 = User("Sancho Panza", "dons.sidekick@adventures.spain")
user2.make_deposit(2000).display_user_balance().make_withdrawal(240).display_user_balance()

# Expected Output:

# Clairy Cherry
# Balance: $254
# Sancho Panza
# Balance: $2000
# Sancho Panza
# Balance: $1760