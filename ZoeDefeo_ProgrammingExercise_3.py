#Zoe Defeo
#Programming Exercise 3
#This program prompts the user for their monthly expenses and how much each of them are. It takes all these expenses
#and sums them into one total, this along with the highest and lowest expense values are displayed.


import functools

#Main function of the program
def main():

    #Initializing dictionary that holds expense type as the keys and their amounts as the values
    expense_list = {}

    #Loop that repeatedly prompts the user to enter expense types and amounts until a blank response is entered
    while True:
        expense = input("Name an expense: ")
        if expense == "":
            break
        expense_list[expense] = int(input("How much is this expense a month? "))

    #Turns values from dictionary into a list for easier sorting
    values = list(expense_list.values())

    #Sums up all expense values into one total.
    total = functools.reduce(lambda x, y: x + y, list(values))

    #Assigns the highest and lowest expense type to variables after checking the list of values.
    highest = [x for x, y in expense_list.items() if y == max(values) ]
    lowest = [x for x, y in expense_list.items() if y == min(values) ]

    #Displays all necessary information about expenses.
    print("\n" + "The total amount you spend on expenses is $" + str(total))
    print("The highest amount you spend is $" + str(max(values)) + " on: " + str(highest))
    print("The lowest amount you spend is $" + str(min(values)) + " on: " + str(lowest))


main()