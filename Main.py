#40 playing cards
#developed by dyyys0ft
#
#imports
import random
import os

#modules
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

    


cardsQty = 5
player1Cards = []
player2Cards = []

listCards = [
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


#empezar el juego

random.shuffle(listCards)
    ###print(listCards)

print("==================================")
print("=== 40  PLAYING  CARDS == GAME ===")
print("==================================\n\n\n")

#opt = int(input("WOULD YOU LIKE TO PLAY VS MACHINE OR VS FRIENDs? (1-2)"))

print("======= PLAYER 1 vs PLAYER 2=====\n")
    #create desk


#create players
print("================================================")
player1 = Player(1,input("Player 1 write your name: "),0,player1Cards,[])
print("================================================\n")
player2 = Player(2,input("Player 2 write your name: "),0,player2Cards,[])
print("================================================\n\n")
print("Players, get READY!!!...\n\n")
print("====" + player1.get_name() + " VS "+ player2.get_name() +"====" )

#define rules
desk = Desk("",True,player1,[player1,player2],"") #refact
#ALL (2)
#NORMAL (COUNT CAIDA AND LIMPIA) (4)


#share cards
player1.playerCards  =  shareCards(listCards,cardsQty)
player2.playerCards  =  shareCards(listCards,cardsQty)

while(player1.get_score() != 40 and player2.get_score() != 40):
    turns = 1
    while(turns < 5):
        
        #================= REFACTORIZAR ==============
        #clean screen
        os.system('clear')
        #player 1 turn 
        
        desk.set_playerTurn(player1)
        desk.showDeskCards()
        print("\n[= " + player1.get_name() + " CARDS =]")
        player1.showCards()
        cardChoosen = player1.chooseCard()
        desk.set_lastCard(cardChoosen)
        desk.caida(cardChoosen) #detect event
        
        
        
        os.system('clear')
        #player 2 turn 
        
        
        desk.set_playerTurn(player2)
        desk.showDeskCards()
        print("\n[= " + player2.get_name() + " CARDS =]")
        cardChoosen = player2.chooseCard()
        desk.set_lastCard(cardChoosen)
        desk.caida(cardChoosen) #detect event
        turns+=1
    
    
    
desk.get_listCards().sort(key = Card.getValue)

print("cartas ordenadas ==== =")
    #analyze combinations   
desk.showDeskCards()







