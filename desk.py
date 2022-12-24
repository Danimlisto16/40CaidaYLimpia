import time
from icecream import ic
from player import Player
from card import Card

cardsOrder = {
    "1":1,
    "2":2,
    "3":2,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "J":8,
    "Q":9,
    "K":10
    }


class Desk:
    def __init__(self, listCards,rules,playerTurn,playersList,lastCard):
        self.listCards = []
        self.rules = rules
        self.playerTurn = playerTurn
        self.playersList = []
        self.lastCard = lastCard
        
    #member functions
    def showDeskCards(self):
        print("========CARDS ON DESK =========")
        print("||                             ||")
        print("||                             ||")
        print(self.listCards,sep = "\t\n")
        print("||                             ||")
        print("||                             ||")
        print("===============================")    
        [print(p.name) for p in self.playersList]
    
        #REFACTORIZAR
    def event(self,card):
        #caida
        #llevada
        #caida y llevada
        #limpia y limpia y llevada
        
        if len(self.listCards) > 0:
            if (Card.getValue(self.lastCard) == Card.getValue(card)):
                self.playerTurn.score(self.playerTurn.score() + 2)        
                self.playerTurn.listSavedCards().append(card)
                self.playerTurn.listSavedCards().append(self.lastCard)
                self.listCards.remove(self.lastCard)
                print(f'\nPlayer: {self.playerTurn.name}  Score: {self.playerTurn.score()}')
                print("==================================")
                print("||             CAIDA            ||")
                print("==================================")
                time.sleep(1)
            else:
                self.lastCard = card
                self.listCards.append(card) #when is a list you need to get it and append it    
        else:
            self.lastCard = card
            self.listCards.append(card)