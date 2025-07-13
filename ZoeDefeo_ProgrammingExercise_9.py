#Zoe Defeo
#Programming Exercise 9
#This program creates a class for a bank account, including methods to adjust various attributes of it.
#The program also has a test function to test these class methods and display all the account information.


class BankAcct:

    #Initializing class attributes
    def __init__(self, name, number, amount, interest):
        self.name = name
        self.number = number
        self.amount = amount
        self.interest = interest

    #Method for giving initial balance.
    def balance(self):
        self.amount = int(input("Enter your balance amount: "))

    #Method for giving initial interest rate.
    def adjust_interest(self):
        self.interest = float(input("Enter the rate of interest: "))

    #Method that adds or subtracts from balance depending on inputs
    def withdraw_deposit(self):
        x = input("Withdraw or Deposit? - (Enter W or D): ")

        while True:
            if x.upper() == 'W':
                y = int(input("How much will you withdraw? "))
                if y <= self.amount:
                    self.amount -= y
                    break
                else:
                    print("Insufficient funds")


            elif x.upper() == 'D':
                y = int(input("How much will you deposit? "))
                self.amount += y
                break

            else:
                print("Invalid Input")

    #Method that adds interest to balance after an input number of days using a compounding interest formula.
    def total_interest(self):
        time = int(input("How many days will interest accrue? "))
        self.amount = self.amount * (1 + ((self.interest / 100) / 365)) ** time

    #Method that gives a string representation of account details.
    def __str__(self):
        return f'Account Holder: {self.name}, Account Number: {self.number}, Balance: ${int(self.amount)}, Interest Rate: {self.interest}%'


#Function to test the class methods
def test():

    #Instantiates the class.
    bank_account = BankAcct("Zoe", "65465199", 500000, 3.74)

    #Prompts each method from the class to fill in and display account details.
    bank_account.balance()
    bank_account.withdraw_deposit()
    bank_account.adjust_interest()
    bank_account.total_interest()
    print(bank_account)




test()