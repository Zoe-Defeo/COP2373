#Zoe Defeo
#Programming Exercise 11
#This program simulates a deck pf cards and generates a random 5 card hand. The user is then prompted to select cards
#from the hand, which are then replaced to create and display a new hand.

import random

#Class that creates the simulated deck of cards
class Deck:

    #Initialzing class attributes
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    #Class method for dealing cards
    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card


#Function that replaces selected cards with new ones and returns the hand
def replace(current_hand, my_deck):

    #Prompts the user to input what cards will be replaced
    discard = str(input('Select card numbers to discard (Separate by commas): '))

    #Splits the input into a readable list
    e = discard.split(',')

    #Deals a new card for each slot the user selected
    for i in e:
        current_hand[i] = my_deck.deal()

    #Returns the new hand after cards have been replaced
    return current_hand


#Main function
def main():

    #Initializing ranks, suits, and deck
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    my_deck = Deck(52)

    #Empty dictionary that will store the created hand
    current_hand = {}

    #Generates cards that are recorded to the dictionary and displayed
    for i in range(5):
        d = my_deck.deal()
        r = d % 13
        s = d // 13
        current_hand[str(f'{i+1}')] = d
        print(f'Card #{i + 1}:', ranks[r], 'of', suits[s])
    print()

    #Selected cards are replaced to form a new hand
    new_hand = replace(current_hand, my_deck)

    #Prints the hand after selected cards have been replaced
    for i in range(5):
        r = new_hand[f'{i+1}'] % 13
        s = new_hand[f'{i+1}'] // 13
        print(f'Card #{i + 1}:', ranks[r], 'of', suits[s])



main()