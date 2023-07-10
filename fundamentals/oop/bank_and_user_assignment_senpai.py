class BankAccount:
    accounts = [] # class attribute, list that holds all accounts
    def __init__(self, interest_rate, start_balance, account_type, account_holder): # initialize BankAccount here
        # print()
        self.interest_rate = interest_rate
        self.balance = start_balance
        self.account_type = account_type
        print(f"{account_type} Account Created for {account_holder}")
        BankAccount.display_account_info(self)
        BankAccount.accounts.append(self) # add each new instance to list

    def deposit(self, amount, account_holder): # Make deposit to account, check for positive deposit amount first
        # print()
        if amount < 0:
            print("Negative deposits are not allowed.")
        else:
            self.balance += amount
            print(f'Depositing {"${:.2f}".format(amount)} to {account_holder}`s {self.account_type} account.')
        BankAccount.display_account_info(self)
        return self

    def withdraw(self, amount, account_holder): # Make withdrawal from account, check that there is a sufficient balance first
        # print()
        if self.balance < amount:
            self.balance -= 5
            print(f"Insufficient balance for requested withdrawal. $5.00 fee applied {account_holder}`s {self.account_type} account.")
        else:
            self.balance -= amount
            print(f'Withdrawing {"${:.2f}".format(amount)} from {account_holder}`s {self.account_type} account.')
        BankAccount.display_account_info(self)
        return self

    def display_account_info(self): # Print current account balance to terminal
        print(f"   Current {self.account_type} account balance is {BankAccount.format_dollars(self.balance)}")
        return self

    def yield_interest(self, account_holder): # Calculate and add interest to account, check if there is a positive balance first
        # print()
        if self.balance <= 0:
            print("No principle balance on account. No interest applied.")
        else:
            interest_earned = round(self.balance*self.interest_rate,2)
            self.balance += interest_earned
            print(f'Interest of {BankAccount.format_dollars(interest_earned)} added to {account_holder}`s {self.account_type} account.')
        BankAccount.display_account_info(self)
        return self
    
    @classmethod
    def print_all_accounts(cls): # Print a list of all instances of BankAccount class to terminal
        i = 1
        for account in BankAccount.accounts:
            print(f'Account #{i}. Balance of {BankAccount.format_dollars(account.balance)}, yielding {"${:.2f}".format(account.interest_rate*100)}%')
            i += 1

    @staticmethod
    def format_dollars(amt): # Simple method to format floats into dollar amounts for display 
        return "${:.2f}".format(amt)
# *********** END *BankAccount* CLASS ********

# *********** BEGIN *User* CLASS ************

# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
# Add a display_user_balance method to the User class that displays user's account balance
# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.


class User():
    # user_accounts = []
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.accounts = {} # creating an empty dictionary attribute for this instance of 'User'. Every time we 'add_account' for this user, a key-value pair will be added to this dictionary

    def add_account(self,interest_rate=.1,amount=0, account_id="Checking"): 
        print()
        # account_holder = conc_name()
        # account_holder = f"{self.first_name} {self.last_name}"
        self.accounts[account_id] = BankAccount(interest_rate, amount, account_id, User.conc_name(self)) # Construct new account instance and add to 'user.accounts' dictionary with key 'account_id' and value of the 'BankAccount' instance
        return self

    def make_deposit (self, amount, account_id):
        print()
        # account_holder = (f"{self.first_name} {self.last_name}")
        self.accounts[account_id].deposit(amount, User.conc_name(self)) # Run the 'BankAccount deposit()' method on the account instance in the 'user.accounts' dictionary with the key of 'account_id'
        return self
    
    def make_withdrawal(self, amount, account_id):
        print()
        # account_holder = (f"{self.first_name} {self.last_name}")
        self.accounts[account_id].withdraw(amount, User.conc_name(self))
        return self
    
    def add_interest(self, account_id):
        print()
        # account_holder = (f"{self.first_name} {self.last_name}")
        self.accounts[account_id].yield_interest(User.conc_name(self))
        return self
    
    def display_user_balance(self):
        print()
        print(f"Here is the status of all accounts for user: {User.conc_name(self)}")
        for account in self.accounts.values(): #loop through each key-value pair in the dictionary. In this 'for' loop, 'account' becomes the *value* for each pair. 'account' then, is a given instance of 'BankAccount' class
            account.display_account_info() # Run the 'BankAccount display_account_info()' method for each 'BankAccount' instance (user bank account).

    def transfer_to_other_user(self,from_account, to_user, to_account, amount):
        print()
        print("***TRANSFER***")
        print(f"Transferring {amount} from {User.conc_name(self)}`s {from_account} to {User.conc_name(to_user)}`s {to_account}.")
        self.accounts[from_account].withdraw(amount, User.conc_name(self))
        to_user.accounts[to_account].deposit(amount, User.conc_name(to_user))

    def conc_name(user):
        return f"{user.first_name} {user.last_name}"

# *********** END *User* CLASS **************

user1 = User("John", "Doe", 26)
user1.add_account(.05,1000,"Savings")
user2 = User("Jane", "Smith", 50)
user2.add_account(.04,500,"Checking")
user1.add_account(0, 350, "Piggy Bank")
user2.make_deposit(300, "Checking")
user1.make_withdrawal(200, "Piggy Bank").make_withdrawal(200, "Piggy Bank")
user1.display_user_balance()
user1.add_account(.01, 200, "Checking").add_interest("Checking").display_user_balance()
user1.transfer_to_other_user("Checking", user2, "Checking", 100)