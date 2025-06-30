#Zoe Defeo
#Programming Exercise 7
#This program prompts the user to enter a paragraph. The program then counts and displays each individual sentence.

#Import module that allows regular expressions to be used.
import re

#Function that scans user paragraph for each individual sentence.
def count(paragraph):

    #Pattern that determines when a sentence in the paragraph ends.
    pattern = r'[A-Z|0-9].*?[.?!](?= [A-Z|0-9]|$)'

    #Scans user paragraph for individual sentences and adds them to list.
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL|re.MULTILINE)

    #Returns list of individual sentences.
    return sentences

#Main function.
def main():

    #Prompts the user to type a paragraph of text.
    paragraph = input("Write a paragraph:" + "\n")

    #Takes the list of individual sentences from count() function.
    total = count(paragraph)

    #Displays total count of sentences.
    print("There are", len(total), "sentences.","\n")

    #Prints each individual sentence.
    for i in total:
        print(i)


main()