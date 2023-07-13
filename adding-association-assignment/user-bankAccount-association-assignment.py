class BankAccount:

    def __init__(self,acct_no,interest_rate=.02,balance=0):
        self.acct_no = acct_no
        self.interest_rate = interest_rate
        self.balance = balance
        # print(f"Account {self.acct_no} Initiated. Balance: ${self.balance}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        # print(f"Account {self.acct_no} Deposit amount: ${amount}")
        return self

    def withdrawal(self,amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            # print(f"Account {self.acct_no} Withdrawal amount: ${amount}")
            return self
        else:
            print(f"You tried to withdrawal ${amount} when your balance was ${self.balance} = Insufficient funds: Charging a $5 fee.")
            self.balance = self.balance - 5.0
            return self

    def display_account_info(self):
        # print(f"Account {self.acct_no} Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.interest_rate
            # print(f"Account {self.acct_no} Interest rate generated increased of: ${self.balance * self.interest_rate}")
            return self
        else:
            pass
            # print(f"no increase possible")


class User:
    def __init__(self, acct_no, interest_rate, balance, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(acct_no,interest_rate, balance)
        # self.savings = BankAccount(.47,2000)
        # self.checking = BankAccount(0,500)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(f"{self.name} deposited ${amount}")
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self
    
    def display_user_balance(self):
        print(f"---------\nUSER: {self.name}\nACCOUNT: {self.account.acct_no}\nBALANCE: ${self.account.balance}")
        return self

user1 = User("00001",.05,205,"Captain Jean-Luc Picard","JLPicard@starfleet.earth")
user1.make_deposit(536).display_user_balance().make_withdrawal(750)
user2 = User("00002",.01,30000,"Jake Sisko","poetjake@creatives.space")
user2.display_user_balance()

# * EVAN'S FEEDBACK: @Gabbe, for future thought, considering you put in a lot of extra work on this assignment, I wouldn’t set a default for the account number.  That is an ‘id’.  To make your code extensible and to prevent multiple accounts with the same ‘id’ you should force the account number to be passed in, or even better, set some sort of logic that will hold the `last_account_no` in the account class itself and then each new account is that plus 1 or some other way of building unique account numbers!