class BankAccount:

    num_of_accounts = 0
    all_instances = []

    def __init__(self, acct_no, interest_rate=.01, balance=0):
        self.acct_no = acct_no
        self.interest_rate = interest_rate
        self.balance = balance
        print(f"Account {self.acct_no} Initiated. Balance: ${self.balance}")
        
        BankAccount.num_of_accounts += 1
        BankAccount.all_instances.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Account {self.acct_no} Deposit amount: ${amount}")
        print(f"New balance: ${self.balance}")
        return self

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            print(f"Account {self.acct_no} withdraw amount: ${amount}")
            return self
        else:
            print(f"You tried to withdraw ${amount} when your balance was ${self.balance} = Insufficient funds: Charging a $5 fee.")
            self.balance - 5.0
            return self

    def display_account_info(self):
        print(f"Account {self.acct_no} Interest Rate: {self.interest_rate} Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.interest_rate
            print(f"Account {self.acct_no} Interest rate generated increased of: ${self.balance * self.interest_rate}")
            return self
        else:
            print(f"no increase possible")
        # while current balance is > 0: current balance * interest rate

    # NINJA BONUS: write a classmethod to print all instances of a Bank Account's info:
    @classmethod
    def get_each_instances_info(cls):
        print(f"EACH INSTANCE AND ITS INFO:\n")
        for account in cls.all_instances:
            BankAccount.display_account_info(account)
        print("\n")


print("\n")
account_000001 = BankAccount("000001",.0495,2.25)
account_000002 = BankAccount("000002",.046,1500)
account_000003 = BankAccount("000003",.03,5000)
print("\n")

account_000001.deposit(10.0).deposit(10.0).deposit(10.0).withdraw(55).yield_interest().display_account_info()
print("\n")

account_000002.display_account_info().deposit(100.75).withdraw(250).withdraw(250).withdraw(250).yield_interest().display_account_info()
print("\n")

account_000003.display_account_info().deposit(4500.0).withdraw(25.45).yield_interest().display_account_info()
print("\n")

print(f"TOTAL NUMBER OF ACCOUNTS: {BankAccount.num_of_accounts}\n")
BankAccount.get_each_instances_info()