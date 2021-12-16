import random
from PySimpleGUI import PySimpleGUI as sg

figures = ["Jack", "Queen", "King", "Ace"]
numbers = list(range(2, 11))
numbers_str = list(map(str, numbers))
cards = numbers_str + figures
 
# defining the names of the suits to be added to each item in the different lists
hearts_name = " of Hearts"
diamonds_name = " of Diamonds"
spades_name = " of Spades"
clubs_name = " of Clubs"

# defining each suit so items can be added to them
hearts = ["","","","","","","","","","","","",""]
diamonds = ["","","","","","","","","","","","",""]
spades = ["","","","","","","","","","","","",""]
clubs = ["","","","","","","","","","","","",""]

# function that adds the suit name to each item of the list (and card)
def suit(suits, suit_name):
    for i in range(len(cards)):
        suits[i] = cards[i] + suit_name

# use of the suit funtion so each element has a card value followed by it's suit
suit(hearts, hearts_name)
suit(diamonds, diamonds_name)
suit(spades, spades_name)
suit(clubs, clubs_name)

Jokers = ["Joker", "Joker"]

blackSuits = clubs + spades
redSuits = diamonds + hearts

#defining a deck as the totality of all the suits (and jokers)
deck = blackSuits + redSuits

sg.theme("DarkAmber")

# funtion center created to facilitate the use of funtions in the following format:
# sg.Stretch(), sg.Text(" "), sg.Stretch()
def center(item):
    return [sg.Stretch(), *item, sg.Stretch()]

# 1st screen shown to player, asks if jokers are to be included and prompts the user to start the game
def WarmUp():
    layout = [
        center([sg.Text("--- Welcome to Rings of Fire ---")]),
        center([sg.Text("Do you wish to include Jokers?")]),
        center([sg.Button("Jokers")]),
        center([sg.Text(
            "Jokers won't be included",
            text_color = "Red",
            justification = "center",
            size=(18,1), key = "DISPLAY")]),
        center([sg.Button("Start Game")])
    ]
    return sg.Window(
        "WarmUp",
        layout = layout,
        size = (250, 150),
        finalize = True)

def Game():
    layout = [
        center([sg.Text("The card number will be displayed here",
        justification = "center",
        size = (30,1),
        key = "NUMBER_DISPLAY")]),
        center([sg.Text("-----Card Taken-----")]),
        center([sg.Text("Your card will be displayed here",
        text_color = "Black",
        size = (30,2),
        justification = "center",
        background_color = "white",
        pad = (10, 10),
        key = "YOUR_CARD")]),
        center([sg.Button("Pull a card", key = "CARD_BUTTON")]),
        center([sg.Button("Restart", key = "RESTART_BUTTON")])
    ]
    return sg.Window(
        "Game",
        layout = layout,
        size = (275, 200),
        finalize = True)

window1, window2 = WarmUp(), None

jokerstate = 0
print("Jokers won't be included")

while True:
    window, event, values = sg.read_all_windows()

    if window == window1 and event == sg.WINDOW_CLOSED:
        print("\n ********* Game Ended by user *********")
        break

    if window1 ==window1 and event == "Jokers" and jokerstate == 0:
        print("Jokers will be included")
        window["DISPLAY"].update(
            text_color = "Green",
            value = "Jokers will be included")
        jokerstate = 1

    elif window == window1 and event == "Jokers" and jokerstate == 1:
        print("Jokers won't be included")
        window["DISPLAY"].update(
            text_color = "Red",
            value = "Jokers won't be included")
        jokerstate = 0

    elif window == window1 and event == "Start Game":
        window1.hide()
        window2 = Game()

        if jokerstate == 0:
             deck = deck
             print("Cards on a deck:", len(deck))

        if jokerstate == 1:
            deck = deck + Jokers
            print("Cards on a deck:", len(deck))

    if window == window2 and event == sg.WINDOW_CLOSED:
        print("\n ********* Game Ended by user *********")
        break

    if window == window2 and event == "RESTART_BUTTON":
        if jokerstate == 0: deck = blackSuits + redSuits
        if jokerstate == 1: deck = blackSuits + redSuits + Jokers
        print("\n********* Game Restarted *********")
        window["NUMBER_DISPLAY"].update(
            value = f"Number of cards on the deck: {len(deck)}")

    if window == window2 and event == "CARD_BUTTON" and len(deck) > 0:
        print(f"\nNumber of cards on the deck: {len(deck)}")
        card = random.choice(deck)
        print("---------", card, "---------")
        deck.remove(card)

        window["NUMBER_DISPLAY"].update(
            value = f"Number of cards on the deck: {len(deck)}")
        window["YOUR_CARD"].update(value = card)

        if card in blackSuits:
            window["YOUR_CARD"].update(text_color = "Black")
        elif card in redSuits:
            window["YOUR_CARD"].update(text_color = "Red")
        else:
            window["YOUR_CARD"].update(text_color = "Green")

    if window == window2 and event == "CARD_BUTTON" and len(deck) == 0:
        window["CARD_BUTTON"].update(text = "Click to exit")
