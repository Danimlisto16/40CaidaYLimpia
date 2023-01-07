#40 playing cards
#developed by dyyys0ft
#
#imports
import random
import os


#modules
from icecream import ic
from card import Card
from desk import Desk
from kindSymbol import kindSymbol as ks
from player import Player


#methods...copy()
def shareCards(listCards,qty):
    playerCards = []
    playerCards = listCards[:qty]
    del(listCards[:qty])
    return playerCards

    

# local variables 
cardsQty = 5
turns = 0
playerNum = 2
share = 0
thereIsWinner = False

#local objects
desk = Desk([],False,False,None,[],None)

initialCards = [
            #HEARTS
            Card(ks.HEARTS,"1"),
            Card(ks.HEARTS,"2"),
            Card(ks.HEARTS,"3"),
            Card(ks.HEARTS,"4"),
            Card(ks.HEARTS,"5"),
            Card(ks.HEARTS,"6"),
            Card(ks.HEARTS,"7"),
            Card(ks.HEARTS,"J"),
            Card(ks.HEARTS,"Q"),
            Card(ks.HEARTS,"K"),
            
            #DIAMONDS
            Card(ks.DIAMONDS,"2"),
            Card(ks.DIAMONDS,"3"),
            Card(ks.DIAMONDS,"1"),
            Card(ks.DIAMONDS,"4"),
            Card(ks.DIAMONDS,"5"),
            Card(ks.DIAMONDS,"6"),
            Card(ks.DIAMONDS,"7"),
            Card(ks.DIAMONDS,"J"),
            Card(ks.DIAMONDS,"Q"),
            Card(ks.DIAMONDS,"K"),
            
            #CLUBS
            Card(ks.CLUBS,"1"),
            Card(ks.CLUBS,"2"),
            Card(ks.CLUBS,"3"),
            Card(ks.CLUBS,"4"),
            Card(ks.CLUBS,"5"),
            Card(ks.CLUBS,"6"),
            Card(ks.CLUBS,"7"),
            Card(ks.CLUBS,"J"),
            Card(ks.CLUBS,"Q"),
            Card(ks.CLUBS,"K"),
            
            #SPADES
            Card(ks.SPADES,"1"),
            Card(ks.SPADES,"2"),
            Card(ks.SPADES,"3"),
            Card(ks.SPADES,"4"),
            Card(ks.SPADES,"5"),
            Card(ks.SPADES,"6"),
            Card(ks.SPADES,"7"),
            Card(ks.SPADES,"J"),
            Card(ks.SPADES,"Q"),
            Card(ks.SPADES,"K")
            
        ]

print("\t\t\t==================================")
print("\t\t\t=== 40  PLAYING  CARDS == GAME ===")
print("\t\t\t==================================\n\n\n")


#cards count till 30
#caida y limpia, all 2

#validate players number
print("=========P L A Y E R S============\n\n")

while True:
    try:
        playerNum = int(input("How many players will play (2 or 4)? "))
        if playerNum != 2 and playerNum != 4:
            print("** You must select 2 or 4 **")
        else:
            break   
    except:
        print('An exception occurred')
print("==================================\n\n")

# Read ruleAll2

print("===========R U L E S==============\n\n")

while True:
    try:
        all2 = input("Do you want to play all 2 (y/n) ?: ")
        if all2 != 'y' and all2 != 'n':
            print("** You must select 'y' or 'n' **")
        else:
            if all2 == 'y':
                desk.ruleAll2 = True
            break   
    except:
        print('An exception occurred')
print("==================================\n\n")

#Read ruleCardsTil30 

while True:
    try:
        cardsUntil30 = input("Do you want to count cards after 30 (y/n)? : ")
        if cardsUntil30 != 'y' and cardsUntil30 != 'n':
            print("** You must select 'y' or 'n' **")
        else:
            if cardsUntil30 == 'y':
                desk.ruleCardsTill30 = True
            break   
    except:
        print('An exception occurred')
print("==================================\n\n")

#>>>>>>>>>>> PRINT A LITTLE INTRODUCTION TO THE RULES >>>>>>>>>>>>>>>

for _ in range(1,playerNum+1):
    player = Player(_,input(f"Player {_} write your name: "),0,[],[])    
    desk.playersList.append(player)

print("Players, get READY!!!...\n\n")

while(not thereIsWinner):
    desk.countCards()
    desk.listCards = []
    desk.lastCard = None

    for p in desk.playersList:
        p.listSavedCards = [] 
        p.savedCards = []

    listCards = initialCards.copy()
    random.shuffle(listCards)


    while(len(listCards) > 0 and not thereIsWinner):
        desk.lastCard = None
        
        for player in desk.playersList:
            player.playerCards = shareCards(listCards,5)
        
        while(len(desk.playersList[-1].playerCards) != 0 and  not thereIsWinner):
            for player in desk.playersList:  
                    
                    desk.playerTurn = player
                    
                    cardChoosen = player.chooseCard(desk)
                    desk.event(cardChoosen)
                    #os.system("clear")
                    print("----------------------------------------------------")
                    desk.showDeskCards()
                    thereIsWinner  = desk.checkWinner()
                    
                    if thereIsWinner:
                        break
    
                    #Read rules before start game, all 2 and carton until 30 DONE

                    #Generate options for take combination of cards










