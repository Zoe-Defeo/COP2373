#Zoe Defeo
#Programming Exercise 1
#This program prompts the user to purchase tickets from a set amount of 20, not being able to buy more than 4 at a time.
#The prompt loops until there are 0 tickets left, ending by displaying total amount of buyers.


#Function that calculates leftover tickets when called
def remainder(tickets,buy):

    tickets -= buy

    #Returns new ticket value for the main function
    return tickets

#Main function of the program
def main():

    #Initializing variables
    tickets = 20
    buyers = 0

    #Repeatedly asks user for input until there are no more tickets left
    while tickets != 0:
        buy = int(input("How many tickets will you buy? "))

        #Asks the user for a new input if their number is not an acceptable amount.
        while buy > 4 or buy > tickets or buy <= 0:
            if buy > 4:
                buy = int(input("You cannot buy more than 4 tickets, select a new amount. "))
            elif buy > tickets:
                buy = int(input("There are only " + str(tickets) + " tickets remaining, select a new amount. "))
            else:
                buy = int(input("Select a valid amount. "))

        #Ticket variable changes to reflect input, calculated by remainder() function
        tickets = remainder(tickets,buy)

        #Outputs remaining number of tickets after the purchase input
        print("There are " + str(tickets) + " tickets left.")

        #Accumulator that tracks the number of times the loop occurs
        buyers += 1

    #Outputs the total number of buyers, being the number of times the loop occurred
    print("Total buyers: " + str(buyers))

main()