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

#local objects
desk = Desk([],True,None,[],None)

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

print("==================================")
print("=== 40  PLAYING  CARDS == GAME ===")
print("==================================\n\n\n")

#validate players number
playerNum = int(input("How many players will play? "))

for _ in range(0,playerNum):
    player = Player(_,input(f"Player {_} write your name: "),0,[],[])    
    desk.playersList.append(player)

print("Players, get READY!!!...\n\n")


while(turns != 2):
    turns += 1
    print("*****TURNS NUMBER ***************************************** "+ str(turns))
    #assign a new set of cards
    listCards = initialCards.copy()
    random.shuffle(listCards)
    #clean desk
    desk.lastCard = None
    desk.listCards = []
    
    for p in desk.playersList:
        p.listSavedCards = [] 
        p.savedCards = []
        
    while(len(listCards) > 0):
        #share the cards to all the players
        for player in desk.playersList:
            player.playerCards = shareCards(listCards,cardsQty)
        
        print(f'"CARDS SHARED ===  {share} ======= "')
        
        while (len(desk.playersList[-1].playerCards) > 0):
            print(f'"======== TURN {turns} ============"')
            
            #================= REFACTOR ==============
            for player in desk.playersList:    
                desk.playerTurn = player
                desk.showDeskCards()
                print("\n[= " + player.name + " CARDS =]")
                player.showCards()  
                limit = random.randint(0, len(player.playerCards)-1)
                cardChoosen = Card(player.playerCards[limit].symbol,player.playerCards[limit].number)
                del player.playerCards[limit]

                desk.listCards.append(cardChoosen)
                
                desk.showDeskCards()
                #desk.caida(cardChoosen) #detect event
                
                #os.system('clear')
        print("\n================== COUNTING CARDS =======================")
        for player in desk.playersList:
            print(f'{ player.name }')
            print(len(player.listSavedCards))
        print("\n=================================================")
    
desk.listCards.sort(key = Card.getValue)

print("cartas ordenadas ==== =")
    #analyze combinations   
desk.showDeskCards()







