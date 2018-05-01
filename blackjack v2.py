import random

cards = []
playerHand = []
computerHand = []
playerValue = []
computerValue = []
cardType = ["Spade", "Hearts", "Diamonds", "Clubs"]
cardValues = ["Ace", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
Values = [[1, 11], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
for i in cardType:
    for j in cardValues:
        cards.append(str(j) + " of " + str(i))#deck created with 52 cards
deck = dict(zip(cards, Values*4))       #deck is made a dict with corresponding values
x = 0
y = 0


def testWin():      #test who won or if it's a draw
    if sum(playerValue) == sum(computerValue):
        print("Draw")
    elif sum(playerValue) == 21:
        print("Blackjack! You win")
    elif sum(computerValue) == 21:
        print("Computer has blackjack you lose")

    if sum(playerValue) > 21:
        if sum(computerValue) < 21:
            print("You lose")
        elif sum(computerValue) > 21:
            print("Draw")
    elif sum(computerValue) > 21:
        if sum(playerValue) < 21:
            print("You win")
        elif sum(playerValue) > 21:
            print("Draw")
    elif sum(playerValue) < 21:
        if sum(computerValue) > 21:
            print("You win!")
        elif sum(computerValue) < sum(playerValue):
            print("You win")
        else:
            print("You lost")


def drawPlayerCard():           #draws a card for the player and stating what he has with corresponding sum of the values
        if len(deck) != 0:
            playing = True
            card = random.choice(list(deck))    #choose a random card
            playerHand.append(card)

            global x
            playerValue.append(deck[playerHand[x]]) #get the value of the card in the player's hand

            while playing:          #when a ace is drawn ask the player if he wants it to be a 1 or 11
                if playerValue[x] == [1, 11]:
                    ace = input("do you want 1 or 11 from your ace? 1/11")
                    if ace == "1":
                        playerValue.pop(x)
                        playerValue.append(1)
                        print(playerValue)
                        playing = False
                    elif ace == "11":
                        playerValue.pop(x)
                        playerValue.append(11)
                        print(playerValue)
                        playing = False
                    else:
                        print("Please select 1 or 11")
                        pass
                else:
                    playing = False
            deck.pop(playerHand[x])
            x += 1

            print("Your Cards are:", playerHand)    #state the cards in the hand of the player and the sum of the value
            print("total value of:", sum(playerValue), "\n")

            if len(playerHand) < 2:     #first round draw 2 cards
                drawPlayerCard()
            else:
                drawComputerCard()
        else:
            print("The deck is empty, let's see who won:")
            testWin()

def drawComputerCard():             #draws a card for the computer and stating what he has with corresponding sum of the values
    aceTest = True

    if sum(computerValue) <= 17:
        card = random.choice(list(deck))
        computerHand.append(card)
        global y
        computerValue.append(deck[computerHand[y]])
        while aceTest:                  #if the computer draws a ace automatically choose 1 or 11 based on the sum of the values of the cards already in his hands
            if computerValue[y] == [1, 11]:
                computerValue.pop(y)
                if sum(computerValue) < 11:
                    computerValue.append(11)
                    aceTest = False
                elif sum(computerValue) >= 11:
                    computerValue.append(1)
                    aceTest = False
            else:
                aceTest = False

        deck.pop(computerHand[y])
        y += 1

        print("the computer has:", computerHand)    #state the cards in the hand of the computer and the sum of the value
        print("total:", sum(computerValue), "\n")


        if len(computerHand) < 2:      #first round draw 2 cards
            drawComputerCard()

        else:
            hitStand()

    else:
        print("the computer stands with a total of:", sum(computerValue))   #make the computer stand if the cards he is holding equal a value of 17 or more
        hitStand()


def hitStand():        #ask if the player wants to hit or stand
        option = input("do you want to hit or stand? [h/s]")

        if option.lower() == "h":
            drawPlayerCard()

        elif option.lower() == "s":
            testWin()

        else:
            print("please say if you want to hit or stand!")
            hitStand()


def start():       #start of the game
    askForStart = input("Do you want to play Blackjack? [y/n]")

    if askForStart == "y":
        drawPlayerCard()

    elif askForStart == "n":
        pass

    else:
        print("please state if you want to start the game")
        start()


start()
