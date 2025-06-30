#Zoe Defeo
#Programming Exercise 6
#

import re

def main():

    zip_pattern = r'\d\d\d\d\d[ -]\d\d\d\d$'
    social_pattern = r'\d\d\d[ -]\d\d[ -]\d\d\d\d$'
    phone_pattern = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d$'

    zip = str(input("Enter Zip Code: "))
    if re.match(zip_pattern, zip):
        print("Valid zip code")
    else:
        print("Invalid zip code")

    social = str(input("Enter Social Security: "))
    if re.match(social_pattern, social):
        print("Valid social security number")
    else:
        print("Invalid social security number")

    phone = str(input("Enter Phone Number: "))
    if re.match(phone_pattern, phone):
        print("Valid phone number")
    else:
        print("Invalid phone number")


main()