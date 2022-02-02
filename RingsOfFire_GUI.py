import random
import PySimpleGUI as sg

figures = ["Jack", "Queen", "King", "Ace"]
numbers = list(range(2, 11))
numbers_str = list(map(str, numbers))
cards = numbers_str + figures
window4Open = 0

#defining the name of each suit so they can be added to the items of each list
hearts_name = " ♥"
diamonds_name = " ♦"
spades_name = " ♠"
clubs_name = " ♣"

#defining the necessary list for each suit
hearts = []
diamonds = []
spades = []
clubs = []

# check what OS is being used so the correct image can be used for it's icon
import os
print(os.name)
if 'nt' in os.name:
    #windows
    icon = "Images/Icon/icon.ico"
else:
    #not windows
    icon = "Images/Icon/icon.png"

# all cards in each deck so rules can be defined to them
Cards = ["Ace", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight",
        "Nine", "Ten", "Jack", "Queen", "King", "Joker"]

# Card = Default Rule
Ace = "Waterfall"
Two = "You"
Three = "Me"
Four = "Whores"
Five = "Category"
Six = "Dicks"
Seven = "Heaven"
Eight = "Mate"
Nine = "Make a Rhyme"
Ten = "Truth or Dare"
Jack = "Make a Rule"
Queen = "Buffle Bill"
King = "Never Have I Ever"
Joker = "Joker"

# Adding all cards to each Suit and also their own suit
def suit(suits, suit_name):
    for i in range(len(cards)):
        suits.append(cards[i])
        suits[i] = cards[i] + suit_name

# use of the suit function so each element has a card value followed by it's suit
suit(hearts, hearts_name)
suit(diamonds, diamonds_name)
suit(spades, spades_name)
suit(clubs, clubs_name)

# defining the list joker as two items so they can be added case the user wants so
Jokers = ["Joker", "Joker"]

# turning it's suit to a black or red list for visual effects
blackSuits = clubs + spades
redSuits = diamonds + hearts

# defining a deck as the totality of all the suits (and jokers)
deck = blackSuits + redSuits

# Defining the "back" boolean for UI uses
back = True

# UI theme
sg.theme("Topanga")

######################## GUI DEFINING ##########################################

# function for centering items on the screen
def center(item):
    return [sg.Stretch(), *item, sg.Stretch()]

# function for adding white spaces to facilitate drawing a Card like figure
def whiteSpace():
    return center([
    sg.Text(size = (20,1),
    background_color = "white",
    pad = (10, 0),)])

# First UI screen
def WarmUp():
    layout = [

        center([sg.Text("--- Welcome to Rings of Fire ---", font = ("Any 11"))]),

        center([sg.Text("Do you wish to include Jokers?")]),

        center([sg.Button("Jokers",
            button_color = "red",
            key = "DISPLAY",
            size = (7, 1),
            pad = (10,5))]),

        center([sg.Button("Play ➤", key = "Start Game", size = (7,1))]),

        center([sg.Button("Change Rules ⛭", key = "Change Rules")])
    ]
    return sg.Window(
        "WarmUp",
        layout = layout,
        size = (250, 200),
        icon = icon,
        finalize = True)

# UI Screen for the Game itself
def Game():
    layout = [
        center([sg.Text("The number of cards will be displayed here",
        justification = "center",
        key = "NUMBER_DISPLAY")]),

        center([sg.Text("-----Card Taken-----", pad = (10,10))]),

        center([sg.Text("Card",
        text_color = "Black",
        size = (20,1),
        background_color = "white",
        pad = (10, 0),
        key = "YOUR_CARD_FACE_TOP")]),

        whiteSpace(),
        whiteSpace(),
        whiteSpace(),

        center([sg.Text("Card",
        text_color = "Black",
        size = (20,1),
        justification = "center",
        background_color = "white",
        pad = (10, 0),
        key = "YOUR_CARD")]),

        center([sg.Text("Rule",
        text_color = "Black",
        size = (20, 1),
        justification = "center",
        background_color = "white",
        pad = (10, 0),
        key = "RULE_DISPLAY")]),

        whiteSpace(),
        whiteSpace(),
        whiteSpace(),

        center([sg.Text("Card",
        text_color = "Black",
        size = (20,1),
        justification = "right",
        background_color = "white",
        pad = (10, 0),
        key = "YOUR_CARD_FACE_BOTTOM")]),

        center([sg.Button("Pull a card",
        pad = (10, 5),
        key = "CARD_BUTTON")]),

        center([sg.Button("Back", key = "RESTART_BUTTON")])
    ]
    return sg.Window(
        "Rings of Fire",
        layout = layout,
        size = (290, 350),
        icon=icon,
        finalize = True)

# UI screen for changing the rules
def RuleDefining():
    layout = [
        center([sg.Text("Defining the Rules")]),
        [sg.Combo(Cards, default_value = "Choose your card",
        key = "combo",
        size = (20,1),
        pad = (10, 20))],

        center([sg.Input("Write your Rule here",
        key = "New_Rule")]),

        center([sg.Button("Next", pad = (10, 20), bind_return_key = True),
        sg.Button("Rules", pad = (10, 20)),
        sg.Button("Back", pad = (10, 20))])
    ]
    return sg.Window(
        "RuleDefining",
        layout = layout,
        size = (300, 190),
        icon=icon,
        finalize = True
    )

# UI screen for checking the rules
def ListRules():
    def printCard(CardFace, CardsFaceValue, CardKey):
        return [sg.Text(f"{CardFace} is for : {CardsFaceValue}", key = CardKey)]

    layout = [
        center([sg.Text("This are the rules:")]),
        center([sg.Text("_"*100)]),

        printCard(Cards[0], Ace, "Ace"),
        printCard(Cards[1], Two, "Two"),
        printCard(Cards[2], Three, "Three"),
        printCard(Cards[3], Four, "Four"),
        printCard(Cards[4], Five, "Five"),
        printCard(Cards[5], Six, "Six"),
        printCard(Cards[6], Seven, "Seven"),
        printCard(Cards[7], Eight, "Eight"),
        printCard(Cards[8], Nine, "Nine"),
        printCard(Cards[9], Ten, "Ten"),
        printCard(Cards[10], Jack, "Jack"),
        printCard(Cards[11], Queen, "Queen"),
        printCard(Cards[12], King, "King"),
        printCard(Cards[13], Joker, "Joker")
    ]
    return sg.Window(
        "ListRules",
        layout = layout,
        size = (250, 400),
        icon=icon,
        finalize = True
    )

# Defining all existing windows and the one(s) to display on launch
window1, window2, window3, window4 = WarmUp(), None, None, None

# Define jokers as not included in default
jokerstate = 0
print("⨯")

def rules():

    def updateFace(face):
        # UI elements on top left and lower right to assimilate a card
        window["YOUR_CARD_FACE_TOP"].update(face)
        window["YOUR_CARD_FACE_BOTTOM"].update(face)

    # Rules based only on each cards face
    if "Ace" in card:
        rule = Ace
        updateFace("ACE")
    elif "2" in card:
        rule = Two
        updateFace("2")
    elif "3" in card:
        rule = Three
        updateFace("3")
    elif "4" in card:
        rule = Four
        updateFace("4")
    elif "5" in card:
        rule = Five
        updateFace("5")
    elif "6" in card:
        rule = Six
        updateFace("6")
    elif "7" in card:
        rule = Seven
        updateFace("7")
    elif "8" in card:
        rule = Eight
        updateFace("8")
    elif "9" in card:
        rule = Nine
        updateFace("9")
    elif "10" in card:
        rule = Ten
        updateFace("10")
    elif "Jack" in card:
        rule = Jack
        updateFace("Jack")
    elif "Queen" in card:
        rule = Queen
        updateFace("Queen")
    elif "King" in card:
        rule = King
        updateFace("King")
    elif "Joker" in card:
        rule = Joker
        updateFace("Joker")
    else:
        rule = card

    return rule

############################### OPEN PROGRAM WINDOW ############################

# Maintains the window open as long as the program is running
while True:
    window, event, values = sg.read_all_windows()

    # Checks if the exit button on the window is pressed and if yes, closes the program
    if window == window1 and event == sg.WINDOW_CLOSED:
        print("\n ********* Game Ended by user *********")
        break

    elif window1 == window1 and event == "DISPLAY":

        # if jokers are included
        if jokerstate == 0:
            print("Jokers will be included")
            window["DISPLAY"].update(
                button_color = "Green")
            jokerstate = 1

        # if jokers are not to be included
        elif jokerstate == 1:
            print("Jokers won't be included")
            window["DISPLAY"].update(
                button_color = "Red")
            jokerstate = 0

    # The Game window is opened by the user
    elif window == window1 and event == "Start Game":
        window1.hide()
        window2 = Game()

        # jokers are not included
        if jokerstate == 0:
             deck = deck

             print("Cards on a deck:", len(deck))

        # jokers are included
        if jokerstate == 1:
            deck = deck + Jokers
            print("Cards on a deck:", len(deck))

    # If the game is already restarted, the Restart button turns to a back Button
    # If the Back Button is pressed the user is promped back to the first window
    elif event == "RESTART_BUTTON" and back == True:
        print("******** Back to Main Menu ********")
        window2.hide()
        window1 = WarmUp()

    elif window == window2 and event == sg.WINDOW_CLOSED:
        print("\n ********* Game Ended by user *********")
        break

    # The Rule Defining window is opened by the user
    elif window == window1 and event == "Change Rules":
        window1.hide()
        window3 = RuleDefining()

    # Restart Button functionality
    elif window == window2 and event == "RESTART_BUTTON":
        # The jokerstate is checked to see which deck is being used, a 52 card or a 54
        #since the items of the deck list where removed they need to be redefined
        if jokerstate == 0: deck = blackSuits + redSuits
        if jokerstate == 1: deck = blackSuits + redSuits + Jokers

        print("\n********* Game Restarted *********")

        # The display for card number is updated to show a full deck
        window["NUMBER_DISPLAY"].update(
            value = f"Number of cards on the deck: {len(deck)}")
        window["YOUR_CARD"].update(
            value = "Card",
            text_color = "Black")
        # Since the decks are full the restart button turns to a Back button
        window["RESTART_BUTTON"].update("Back")
        window["RULE_DISPLAY"].update(value = "Rule")
        back = True

    elif window == window2 and event == "CARD_BUTTON" and len(deck) > 0:
        print(f"\nNumber of cards on the deck: {len(deck)}")
        # Random card "pulled" from the deck and removed so it can't be "pulled" twice
        card = random.choice(deck)
        print("---------", card, "---------")
        deck.remove(card)
        print("is for", rules())

        # Card display updated to the value of the "pulled" card
        window["NUMBER_DISPLAY"].update(
            value = f"Number of cards on the deck: {len(deck)}")
        window["YOUR_CARD"].update(value = card)
        window["RULE_DISPLAY"].update(value = "is for " + rules())

        # Visual Representation of the cards Suit through it's color
        if card in blackSuits:
            window["YOUR_CARD"].update(text_color = "Black")
            window["YOUR_CARD_FACE_TOP"].update(text_color = "Black")
            window["YOUR_CARD_FACE_BOTTOM"].update(text_color = "Black")
        elif card in redSuits:
            window["YOUR_CARD"].update(text_color = "Red")
            window["YOUR_CARD_FACE_TOP"].update(text_color = "Red")
            window["YOUR_CARD_FACE_BOTTOM"].update(text_color = "Red")
        else:
            window["YOUR_CARD"].update(text_color = "Green")
            window["YOUR_CARD_FACE_TOP"].update(text_color = "Green")
            window["YOUR_CARD_FACE_BOTTOM"].update(text_color = "Green")

        if jokerstate == 0 and len(deck) != 52:
            window["RESTART_BUTTON"].update("Restart")
            back = False

        elif jokerstate == 1 and len(deck) != 54:
            window["RESTART_BUTTON"].update("Restart")
            back = False

        else:
            window["RESTART_BUTTON"].update("Back")
            back = True

    # No more Cards in deck, update Card Display to Game Over
    elif window == window2 and event == "CARD_BUTTON" and len(deck) == 0:
        window["YOUR_CARD"].update("Game Over")


    elif window == window3 and event == sg.WINDOW_CLOSED:
        print("\n ********* Game Ended by user *********")
        break

    elif window == window3 and event == "Back":
        window3.hide()
        window1 = WarmUp()

        if window4Open == 1:
            # Windows are Closed before opening to avoid multiple instances of the same windows
            window1.close()
            window1 = WarmUp()
            window4.close()
            window4 = ListRules()
            # Getting the location of window1 in a list (x, y) format
            loc1 = window1.CurrentLocation()
            # Splitting the List into two variables so they can be used in Move()
            window1X, window1Y = loc1
            # Defining the new window to be created aside the main one
            window4.Move(window1X + 270 , window1Y - 100)

    elif window == window3 and event == "Next":

        window["New_Rule"].update(" ")

        # list of rules that are not accepted since most of them are part of the program itself and error checking
        dont = [
        "Write your Rule here",
        "No Rule was defined",
        "Card not defined",
        " ",
        ""]

        # Rule changing for each cards face
        if values["New_Rule"] not in dont :
            if values["combo"] == "Ace":
                Ace = values["New_Rule"]
                print("Ace was changed to :", values["New_Rule"])
            elif values["combo"] == "Two":
                Two = values["New_Rule"]
                print("Two was changed to :", values["New_Rule"])
            elif values["combo"] == "Three":
                Three = values["New_Rule"]
                print("Three was changed to :", values["New_Rule"])
            elif values["combo"] == "Four":
                Four = values["New_Rule"]
                print("Four was changed to :", values["New_Rule"])
            elif values["combo"] == "Five":
                Five = values["New_Rule"]
                print("Five was changed to :", values["New_Rule"])
            elif values["combo"] == "Six":
                Six = values["New_Rule"]
                print("Six was changed to :", values["New_Rule"])
            elif values["combo"] == "Seven":
                Seven = values["New_Rule"]
                print("Seven was changed to :", values["New_Rule"])
            elif values["combo"] == "Eight":
                Eight = values["New_Rule"]
                print("Eight was changed to :", values["New_Rule"])
            elif values["combo"] == "Nine":
                Nine = values["New_Rule"]
                print("Nine was changed to :", values["New_Rule"])
            elif values["combo"] == "Ten":
                Ten = values["New_Rule"]
                print("Ten was changed to :", values["New_Rule"])
            elif values["combo"] == "Jack":
                Jack = values["New_Rule"]
                print("Jack was changed to :", values["New_Rule"])
            elif values["combo"] == "Queen":
                Queen = values["New_Rule"]
                print("Queen was changed to :", values["New_Rule"])
            elif values["combo"] == "King":
                King = values["New_Rule"]
                print("King was changed to :", values["New_Rule"])
            elif values["combo"] == "Joker":
                Joker = values["New_Rule"]
                print("Joker was changed to :", values["New_Rule"])
            else:
                print("Error")
                window["New_Rule"].update("Card not defined")

        else: window["New_Rule"].update("No Rule was defined")

        # CHeking if the List Rules window is opened or not so it is updated and correctly positioned
        if window4Open == 1:
            window4.close()
            window4 = ListRules()
            window4.Move(window3X + 310 , window3Y - 100)

    elif window == window3  and event == "Rules":
        if window4Open == 0:
            window4 = ListRules()
            window4Open = 1
            loc3 = window3.CurrentLocation()
            window3X, window3Y = loc3
            window4.Move(window3X + 310 , window3Y - 100)

    elif window == window4 and event == sg.WINDOW_CLOSED:
        window.close()
        window4Open = 0
