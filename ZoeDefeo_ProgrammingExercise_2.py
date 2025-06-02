#Zoe Defeo
#Programming Exercise 2
#This program prompts the user to type out an email message and scans it for commonly used spam email words and phrases
#from a set list. The program counts these instances and attributes them to a score, spam likelihood rating,
#and a list of the spam words found in the user's email, all of which are displayed at the end.


#Function that scans the user email message for common spam words and phrases
def spam_check(email):

    #List of common spam email words and phrases
    spam_list = ["free", "money", "cash", "information", "guarantee", "special", "offer", "deal", "value", "promise",
                 "best", "earn", "price", "account", "urgent", "eligible", "click", "opportunity", "claim", "exclusive",
                 "prize", "limited time", "save", "congratulations", "win", "% off", "call", "chance", "now", "fast"]

    #Initializing variables
    spam_score = 0
    email_spam = []

    #Adds to the spam score and email word list every time a spam word is detected, repeated until every spam word
    #from the set list is checked
    for word in spam_list:
        n = spam_score
        spam_score += email.lower().count(word)
        if n != spam_score:
            email_spam.append(word)

    #Returns total number of times spam words appear in email and the specific words detected.
    return spam_score, email_spam


#Main function of the program
def main():

    #Prompts the user to input an email message
    email = input("Write an email message:" + "\n")

    #Calls the spam_check function to return its values
    spam_score, email_spam = spam_check(email)

    #Calculates the ratio of detected spam words to total number of words in the email and makes it a percent.
    spam_percent = spam_score / len(email.split()) * 200

    #Prints all the found information.
    print("\n"+ "Your spam score was " + str(spam_score)
          + ", the likelihood your email is spam is " + str(int(spam_percent)) + "%")
    print("Suspected spam words in your email: " + ", ".join(email_spam))


main()