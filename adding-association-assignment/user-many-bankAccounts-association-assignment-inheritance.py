class BankAccount:

    num_of_accounts = 0
    all_acct_instances = []

    def __init__(self, interest_rate = .02,balance = 0):
        # self.acct_no = acct_no
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
        print(f"ACCOUNT INFO:\nInterest rate: {self.interest_rate}. Balance: ${self.balance}.")
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



#! CHILD
class CheckingAccount(BankAccount):
    def __init__(self, interest_rate, balance = 0):
        super().__init__(interest_rate, balance)
    def deposit_to_checking(self, amount):
        super().deposit(amount)
        return self
    def withdraw_checking(self, amount):
        super().withdraw(amount)
        return self
    def write_check(self, amount):
        super().withdraw(amount)
        return self      
    def display_info_checking(self):# display_account_info or display_checking_account_info?
        return super().display_account_info()



#! CHILD
class SavingsAccount(BankAccount):
    def __init__(self, interest_rate = .04, balance = 0): 
        super().__init__(interest_rate, balance)
    def deposit_savings(self, amount):
        super().deposit(amount)
        return self
    def withdraw(self, amount):
        super().withdraw(amount)
        return self
    def yield_savings_interest(self): # is this a classmethod?
        super().yield_interest(.04)
        return self
    def display_info_savings(self):
        super().display_account_info()
        return self



#! CHILD
class RetirementAccount(BankAccount):
    def __init__(self, interest_rate = .05, is_roth = True, balance = 0):
        super().__init__(interest_rate, balance)
        self.is_roth = is_roth
    def deposit_retirement(self, amount):
        super().deposit(amount)
        return self
    def withdraw_retirement(self, amount, is_early):
        if is_early:
            amount *= 1.10
            super().withdraw(amount)
            return self
        else:
            print("Congratulations for waiting until you are 62.5. You may now withdraw from this account without penalties.")
            super().withdraw(amount)
            return self
    def yield_retirement_interest(self): # is this a classmethod?
        super().yield_interest()
        return self
    def display_info_retirement(self):
        super().display_account_info()
        return self



#! ASSOCIATED CLASS
class User:
    def __init__(self, interest_rate, balance, name, email): # why is interest_rate here?
        self.name = name
        self.email = email
        # self.account = BankAccount(acct_no, interest_rate, balance) # use this instead of following 3 lines if scrapping inheritance code
        self.checking = BankAccount(balance)
        self.savings = BankAccount(interest_rate, balance)
        self.retirement = BankAccount(interest_rate, is_roth = True, balance = 0)
    def user_makes_deposit_checking(self, amount):
        self.checking.deposit(amount)
        print(f"{self.name} deposited ${amount}.")
        return self
    def user_makes_withdrawal_checking(self, amount):
        self.checking.withdraw(amount)
        return self
    def user_display_balance_checking(self):
        print(f"USER'S INFO: {self.name}. CHECKING BALANCE: ${self.checking.balance}.")
        return self
    # BONUS:
    # add conditionals for account choice
    # create transfer_money method taking in amount and other_user, do i need a method to make and receive or just make and then its received as a deposit?
    # def transfer_money(self, acct_no, amount, other_user):
    #     pass


#! TEST
print("\n")

user1 = User(.05,205,"Captain Jean-Luc Picard","JLPicard@starfleet.earth")
user1.user_makes_deposit_checking(536).user_display_balance_checking().ser_makes_withdrawal_checking(750).user_display_balance_checking()
print("\n")

user2 = User(.01,30000,"Jake Sisko","poetjake@creatives.space")
user2.user_display_balance_checking()
print("\n")

# account_000036 = CheckingAccount("000036", .236, 40)
# account_000036.write_check(200)