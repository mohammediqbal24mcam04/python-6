class BankAccount:
    def __init__(self, name, account_number, account_type, balance):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.balance}")

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

# User input
name = input("Enter your name: ")
account_number = input("Enter account number: ")
account_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, account_number, account_type, balance)

# Operations
account.display_details()
account.deposit(float(input("Enter amount to deposit: ")))
account.withdraw(float(input("Enter amount to withdraw: ")))
account.display_details()
