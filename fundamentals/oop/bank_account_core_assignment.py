    # DONE__init__ method, 
    # DONE if balance amount is given set it to that, otherwise default to $0 balance
    # interest rate in decimal format e.g.(.01), ?put interest rate as first parameter so that balance can be optional?
    #  
    # Should be a list of accounts for class (class attribute)
    # Methods:
    # DONE: Deposit(self, amount)
    # DONE: Withdraw (self, amount) - if insufficient funds deduct $5
    # DONE: display_account_info(self) - print "balance $100.00"
    # DONE: yield_interest(self) - check for positive balance, then increase balance by interest rate * balance

class BankAccount:
    accounts = [] # class attribute, list that holds each account
    # ... __init__ goes here
    def __init__(self, interest_rate=0, start_balance=0):
        self.interest_rate = interest_rate
        self.balance = start_balance
        print("Account Created")
        BankAccount.display_account_info(self)
        BankAccount.accounts.append(self) # add each new instance to list

    def deposit(self, amount):
        if amount < 0:
            print("Negative deposits are not allowed.")
        else:
            self.balance += amount
            print(f'Depositing {"${:.2f}".format(amount)}.')
        BankAccount.display_account_info(self)
        return self

    def withdraw(self, amount=0):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient balance for requested withdrawal. $5.00 fee applied")
        else:
            self.balance -= amount
            print(f'Withdrawing {"${:.2f}".format(amount)}.')
        BankAccount.display_account_info(self)
        return self

    def display_account_info(self):
        print(f"Current account balance is {BankAccount.format_dollars(self.balance)}")
        print()
        return self

    def yield_interest(self):
        if self.balance <= 0:
            print("No principle balance on account. No interest applied.")
        else:
            interest_earned = round(self.balance*self.interest_rate,2)
            self.balance += interest_earned
            print(f'Interest of {BankAccount.format_dollars(interest_earned)} added to account.')
        BankAccount.display_account_info(self)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        i = 1
        for account in BankAccount.accounts:
            print(f'Account #{i}. Balance of {BankAccount.format_dollars(account.balance)}, yielding {"${:.2f}".format(account.interest_rate*100)}%')
            i += 1

    @staticmethod
    def format_dollars(amt):
        return "${:.2f}".format(amt)

user1 = BankAccount(.01,1000)
user2 = BankAccount(.05)
user1.deposit(100).deposit(200).deposit(100).withdraw(50).yield_interest()
user2.deposit(200). deposit(50).withdraw(260).withdraw(245).yield_interest()
BankAccount.print_all_accounts()