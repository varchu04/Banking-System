class Bank:
    def __init__(self):
        self.balance = 0

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


def create_account(accounts, account_number):
    if account_number not in accounts:
        accounts[account_number] = Bank()
        print("Account created successfully.")
    else:
        print("Account already exists.")


def main():
    accounts = {}

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
            create_account(accounts, account_number)
        elif choice == '2':
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    if amount <= 0:
                        print("Invalid amount. Please enter a positive value.")
                    else:
                        accounts[account_number].deposit(amount)
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