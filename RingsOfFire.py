import random

clubs = ["Ace of clubs", "2 of clubs", "3 of clubs",
       "4 of clubs", "5 of clubs", "6 of clubs",
       "7 of clubs", "8 of clubs", "9 of clubs",
       "10 of clubs", "Jack of clubs",
       "Queen of clubs", "King of clubs"]

spades = ["Ace of spades", "2 of spades", "3 of spades",
        "4 of spades", "5 of spades", "6 of spades",
        "7 of spades", "8 of spades", "9 of spades",
        "10 of spades", "Jack of spades",
        "Queen of spades", "King of spades"]

diamonds = ["Ace of diamonds", "2 of diamonds", "3 of diamonds",
          "4 of diamonds", "5 of diamonds", "6 of diamonds",
          "7 of diamonds", "8 of diamonds", "9 of diamonds",
          "10 of diamonds", "Jack of diamonds",
          "Queen of diamonds", "King of diamonds"]

hearts = ["A of hearts", "2 of hearts", "3 of hearts",
        "4 of hearts", "5 of hearts", "6 of hearts",
        "7 of hearts", "8 of hearts", "9 of hearts",
        "10 of hearts", "Jack of hearts",
        "Queen of hearts", "King of hearts"]

jokers = ["Joker", "Joker"]

blackSuits = clubs + spades
redSuits = diamonds + hearts

deck = blackSuits + redSuits

addjokers = input("Do you wish to include Jokers? (y/n)\n>>>")
print()

if addjokers == "y" or addjokers == "yes":
    deck = deck + jokers
    print("Jokers will be included on the deck\n")

if addjokers == "n" or addjokers == "no":
    deck = deck
    print("Jokers won't be included on the deck\n")

else:
    print("The input is not valid")
    print("Jokers won't be included")
    print()

while len(deck) != 0:

    print("Number of cards on deck:", len(deck))
    print()
    print("Do you want to draw a card? (y/n)")
    choice = input("\n>>>")
    print()

    if choice == "y" or choice == "yes":

        card = random.choice(deck)

        print("---------", card, "---------")
        deck.remove(card)

    elif choice == "n" or choice == "no":
        print("The game is Over.")
        exit()

    else : print(f"The input of: {choice} is not valid, please choose between Yes or No")
