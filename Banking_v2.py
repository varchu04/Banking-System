import os

import re

def is_valid_indian_phone_number(phone_number):
    # Define the regex pattern for a valid Indian phone number
    pattern = re.compile(r'^(?:\+?91)?[6789]\d{9}$')
    
    # Check if the phone number matches the pattern
    if pattern.match(phone_number):
        return True
    else:
        return False
    
def is_valid_name(name):
    # Remove spaces from the name and check if all characters are alphabetic
    if not name.replace(" ", "").isalpha():
        raise ValueError("Invalid name. Please enter a valid name.")
    return True

class PersonalInformation:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    

class Bank:
    def __init__(self, name, num):
        self.balance = 0
        self.personal_information = PersonalInformation(name=name, num=num)

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount ${amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount ${amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def check_balance(self):
        print(f"Your current balance: ${self.balance:.2f}")

def create_account(accounts, account_number, account_holder, account_holder_number):
    if account_number not in accounts:
        accounts[account_number] = Bank(account_holder, account_holder_number)
        print("Account created successfully.")
    else:
        print("Account already exists.")

def save_accounts(accounts, filename):
    with open(filename, 'w') as file:
        for account_number, bank_obj in accounts.items():
            file.write(f"{account_number}:{bank_obj.balance}:{bank_obj.personal_information.name}:{bank_obj.personal_information.num}\n")

def load_accounts(filename):
    accounts = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                account_number, balance, name, mobile_number = line.strip().split(':')
                accounts[account_number] = Bank(name, mobile_number)
                accounts[account_number].balance = float(balance)
    return accounts

def main():
    filename = "accounts.txt"
    accounts = load_accounts(filename)

    print("Welcome to Our Bank!")

    while True:
        print("\nPlease select an option:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            account_number = input("Enter your account number: ")
            account_holder = input("Enter Acc Holder Name: ")
            try:
                is_valid_name(account_holder)
                print("Valid name entered:", account_holder)
                account_holder_num = input("Enter your Mobile Number: ")
                try:
                    if account_holder_num:
                        if is_valid_indian_phone_number(account_holder_num):
                            account_holder_num = account_holder_num
                        else:
                            raise ValueError("Invalid Indian phone number")
                    else:
                        raise ValueError("Invalid Indian phone number")

                    create_account(accounts, account_number, account_holder, account_holder_num) 
                except ValueError as er:
                    print("Invalid Indian phone number")
            except ValueError as e:
                print(e)
            
        elif choice == '2':
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    if amount <= 0:
                        print("Invalid amount. Please enter a positive value.")
                    else:
                        accounts[account_number].deposit(amount)
                        save_accounts(accounts, filename)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            else:
                print("Account not found. Please create an account first.")
        elif choice == '3':
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    if amount <= 0:
                        print("Invalid amount. Please enter a positive value.")
                    else:
                        accounts[account_number].withdraw(amount)
                        save_accounts(accounts, filename)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            else:
                print("Account not found. Please create an account first.")
        elif choice == '4':
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found. Please create an account first.")
        elif choice == '5':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
