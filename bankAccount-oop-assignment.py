class BankAccount:

    def __init__(self,acct_no,interest_rate,balance):
        self.acct_no = acct_no
        self.interest_rate = interest_rate
        self.balance = balance
        print(f"Account {self.acct_no} Initiated. Balance: {self.balance}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Account {self.acct_no} Deposit amount: {amount}")
        return self

    def withdrawal(self,amount):
        self.balance = self.balance - amount
        print(f"Account {self.acct_no} Withdrawal amount: {amount}")
        return self

    def display_account_info(self):
        print(f"Account {self.acct_no} Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance + self.balance * self.interest_rate
        print(f"Account {self.acct_no} increased by: {self.balance * self.interest_rate}")
        return self
        # while current balance is > 0: current balance * interest rate
account_000001 = BankAccount("000001",.0495,20000)
# account_000002 = BankAccount("000002",.046,1500)
# account_000003 = BankAccount("000003",.03,5000)

account_000001.display_account_info().deposit(10000.0).withdrawal(25).display_account_info().yield_interest()
# account_000002.display_account_info().deposit(100.75).withdrawal(250).display_account_info()
# account_000003.display_account_info().deposit(4500.0).withdrawal(25).display_account_info()