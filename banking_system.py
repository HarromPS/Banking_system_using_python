# Python program to create bank account class
# With both a deposit() and a withdraw() function

# Has a function to show user account status
# Stores details about amount

# Allows for deposit, withdraw and to view balance available

print("==========================================")

print("\nCreate New User Account\n ")
name = input("Enter Your Name\n==>")
age = int(input("Enter your age \n==>"))
gender = input("Enter your Gender (Male/Female/Others)\n==>")

print("User Details as follows\n ")
print("*******************************************\n")
print("\nUSER NAME\n ", name)
print("\nUSER AGE\n ", age)
print("\nUSER GENDER\n ", gender)


class user():
    def __init__(self):
        self.balance = 0
        print("\nWelcome User To Deposit  & Withdrawl Machine \n")

    def deposit(self):
        amount = float(input("Enter Amount to be Deposited: \nRs."))
        self.balance += amount
        print("\n Amount Deposited:\nRs.\n", amount)

    def withdraw(self):

        amount = float(input("Enter Amount to be Withdrawn: \nRs.\n"))
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:\nRs.\n", amount)
        else:
            print("Insufficient balance \nAdd money to your account\n")

    def display(self):
        print("Net Available Balance=\nRs.\n", self.balance)

# Driver code
# creating an object of class
s = user()

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()

print("\nThank You for using our services\n")
print("==========================================")
