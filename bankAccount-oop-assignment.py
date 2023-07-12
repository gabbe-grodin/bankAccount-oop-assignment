class BankAccount:

    def __init__(self,acct_no,interest_rate,balance):
        self.acct_no = acct_no
        self.interest_rate = interest_rate
        self.balance = balance
        print(f"Account {self.acct_no} Initiated. Balance: ${self.balance}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Account {self.acct_no} Deposit amount: ${amount}")
        return self

    def withdrawal(self,amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            print(f"Account {self.acct_no} Withdrawal amount: ${amount}")
            return self
        else:
            print(f"You tried to withdrawal ${amount} when your balance was ${self.balance} = Insufficient funds: Charging a $5 fee.")
            self.balance - 5.0
            return self

    def display_account_info(self):
        print(f"Account {self.acct_no} Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance + self.balance * self.interest_rate
            print(f"Account {self.acct_no} Interest rate generated increased of: ${self.balance * self.interest_rate}")
            return self
        else:
            print(f"no increase possible")
        # while current balance is > 0: current balance * interest rate
account_000001 = BankAccount("000001",.0495,2.25)
account_000002 = BankAccount("000002",.046,1500)
account_000003 = BankAccount("000003",.03,5000)

account_000001.deposit(10.0).deposit(10.0).deposit(10.0).withdrawal(55).yield_interest().display_account_info()
account_000002.display_account_info().deposit(100.75).withdrawal(250).withdrawal(250).withdrawal(250).yield_interest().display_account_info()
account_000003.display_account_info().deposit(4500.0).withdrawal(25.45).yield_interest().display_account_info()