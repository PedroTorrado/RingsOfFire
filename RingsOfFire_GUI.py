import random
from PySimpleGUI import PySimpleGUI as sg

figures = ["Jack", "Queen", "King", "Ace"]
numbers = list(range(2, 11))
numbers_str = list(map(str, numbers))
cards = numbers_str + figures

hearts_name = " of Hearts"                                      # defining the names of the suits to be added to each item in the different lists
diamonds_name = " of Diamonds"
spades_name = " of Spades"
clubs_name = " of Clubs"

hearts = ["","","","","","","","","","","","",""]               # defining each suit so items can be added to them
diamonds = ["","","","","","","","","","","","",""]
spades = ["","","","","","","","","","","","",""]
clubs = ["","","","","","","","","","","","",""]

def suit(suits, suit_name):                                     # function that adds the suit name to each item of the list (and card)
    for i in range(len(cards)):
        suits[i] = cards[i] + suit_name

suit(hearts, hearts_name)                                       # use of the suit funtion so each element has a card value followed by it's suit
suit(diamonds, diamonds_name)
suit(spades, spades_name)
suit(clubs, clubs_name)

Jokers = ["Joker", "Joker"]

blackSuits = clubs + spades
redSuits = diamonds + hearts

deck = blackSuits + redSuits                                    # defining a deck as the totality of all the suits (and jokers)

sg.theme("DarkAmber")

def center(item):                                               # funtion center created to facilitate the use of funtions in the following format:
    return [sg.Stretch(), *item, sg.Stretch()]                  # sg.Stretch(), sg.Text(" "), sg.Stretch()


                                                                # 1st screen shown to player, asks if jokers are to be included and prompts the user to start the game
def WarmUp():
    layout = [
                                                                #defining different objects from PySimpleGUI to use on the first window
        center([sg.Text("--- Welcome to Rings of Fire ---")]),  # Top Text
        center([sg.Text("Do you wish to include Jokers?")]),    # Under text question
        center([sg.Button("Jokers")]),                          # Button Text
        center([sg.Text(
            "Jokers won't be included",                         # Jokers state displayed
            text_color = "Red",
            justification = "center",
            size=(18,1), key = "DISPLAY")]),
        center([sg.Button("Start Game")])                       # Start Button
    ]
    return sg.Window(
        "WarmUp",                                               # Window Name / Text
        layout = layout,                                        # defining the layout designed before
        size = (250, 150),                                      # Window Size
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

window1, window2 = WarmUp(), None                                       # defining two windows and declaring the WarmUp() funtion as window1

jokerstate = 0                                                          # defining a the state of jokers as non included to later be used
print("Jokers won't be included")

while True:
    window, event, values = sg.read_all_windows()                       # Maintains the window open as long as the program is running

    if window == window1 and event == sg.WINDOW_CLOSED:                 # If exit button is pressed by the user
        print("\n ********* Game Ended by user *********")              # prints a message in cmd showing the game was ended by the user
        break                                                           # And closes the loop and therefore the program

    if window1 ==window1 and event == "Jokers" and jokerstate == 0:     # If the button to include jokers is pressed
        print("Jokers will be included")                                # a message is printed in cmd informing the joker state
        window["DISPLAY"].update(                                       # the text display of joker state changes color representing it's state (green = included)
            text_color = "Green",
            value = "Jokers will be included")
        jokerstate = 1                                                  # joker state is 1 when jokers are included

    elif window == window1 and event == "Jokers" and jokerstate == 1:   # If the button to include jokers is pressed again
        print("Jokers won't be included")                               # a message is printed in cmd informing the joker state
        window["DISPLAY"].update(                                       # the text display of joker state changes color representing it's state (red = not included)
            text_color = "Red",
            value = "Jokers won't be included")
        jokerstate = 0                                                  # joker state is 0 when jokers are not included

    elif window == window1 and event == "Start Game":                   # If Start Game is pressed
        window1.hide()                                                  # Window1 (WarmUp() window) is closed or "hiden"
        window2 = Game()                                                # Window2 (Game() window) is opened

        if jokerstate == 0:                                             # if jokerstate is zero it means the jokers shouldn't be included in the deck
             deck = deck                                                # so that jokers aren't included the list deck is equal to itself
                                                                        # this step isn't needed but makes it easier to compare the two if statements and pratically changes nothing
             print("Cards on a deck:", len(deck))                       # prints to CMD the amount of cards on a deck

        if jokerstate == 1:                                             # if jokerstate is one ir means the jokers should be included in the deck
            deck = deck + Jokers                                        # to include jokers the jokers list is added to the deck list making it a 54 item list
            print("Cards on a deck:", len(deck))

    if window == window2 and event == sg.WINDOW_CLOSED:                 # sg.WINDOW_CLOSED is the action of clicking the top right exit button of a window
        print("\n ********* Game Ended by user *********")
        break                                                           # by breaking the while loop the window and therefore the program closes

    if window == window2 and event == "RESTART_BUTTON":                 # if the restart button is pressed
                                                                        # the jokerstate is checked to see which deck was being used, a 52 card or a 54
        if jokerstate == 0: deck = blackSuits + redSuits                # since the items of the deck list where removed this needs to be recomposed by the lists from the biggining
        if jokerstate == 1: deck = blackSuits + redSuits + Jokers       # same here but including also the jokers
        print("\n********* Game Restarted *********")
        window["NUMBER_DISPLAY"].update(                                # the display which shows the number of cards in a deck gets updated to show the deck is full
            value = f"Number of cards on the deck: {len(deck)}")

    if window == window2 and event == "CARD_BUTTON" and len(deck) > 0:  # if a card is pulled from the deck
        print(f"\nNumber of cards on the deck: {len(deck)}")            # the numbers of card on the deck is presented on a CMD line
        card = random.choice(deck)                                      # a random item from the list deck is pulled and placed on the string variable card
        print("---------", card, "---------")                           # the card is shown on a CMD line
        deck.remove(card)                                               # the card is removed from the deck

        window["NUMBER_DISPLAY"].update(                                # the display which holds the number of cards in a deck is updated to the number of cards
            value = f"Number of cards on the deck: {len(deck)}")
        window["YOUR_CARD"].update(value = card)                        # the card is displayed on its display

        if card in blackSuits:                                          # if the card belongs to one of the black suits it's shown in black lettering
            window["YOUR_CARD"].update(text_color = "Black")
        elif card in redSuits:                                          # if the card belongs to one of the red suits it's shown in red lettering
            window["YOUR_CARD"].update(text_color = "Red")
        else:                                                           # if the card is a Joker it's shown in green lettering
            window["YOUR_CARD"].update(text_color = "Green")

    if window == window2 and event == "CARD_BUTTON" and len(deck) == 0: # if the deck is empty the button to pull a card is updated to "Click to exit"
        window["CARD_BUTTON"].update(text = "Click to exit")
        break
