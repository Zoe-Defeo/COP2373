#Zoe Defeo
#Programming Exercise 6
#This program prompts the user for a phone number, zip code, and social security number.
#Using regular expressions, the program checks and displays if these numbers are valid or not.

#Import module to allow regular expressions to be used.
import re

#Main function
def main():

    #Regular expression patterns to compare against input.
    zip_pattern = r'\d\d\d\d\d[ -]\d\d\d\d$'
    social_pattern = r'\d\d\d[ -]\d\d[ -]\d\d\d\d$'
    phone_pattern = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d$'

    #Prompt user for zip code input
    zip = str(input("Enter Zip Code: "))

    #Compare input with corresponding pattern, print valid if matching, invalid if not.
    if re.match(zip_pattern, zip):
        print("Valid zip code")
    else:
        print("Invalid zip code")

    #Prompt user for social security input.
    social = str(input("Enter Social Security: "))

    #Compare input with corresponding pattern, print valid if matching, invalid if not.
    if re.match(social_pattern, social):
        print("Valid social security number")
    else:
        print("Invalid social security number")

    #Prompt user for phone number input.
    phone = str(input("Enter Phone Number: "))

    #Compare input with corresponding pattern, print valid if matching, invalid if not.
    if re.match(phone_pattern, phone):
        print("Valid phone number")
    else:
        print("Invalid phone number")


main()
