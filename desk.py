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
        [print(" >"+p.name + " "+ str(p.score) ) for p in self.playersList]
    
    @staticmethod
    def orderCards(cardsList):
        if len(cardsList) > 0:
            listOrderedCards = cardsList.copy()
            listOrderedCards.sort(key = Card.getValue)
            return listOrderedCards 
        return []


    def event(self,card):
        
        isCaida = False
        isLlevada = False
        cardValue = Card.getValue(card)

        
        orderedCards = self.orderCards(self.listCards)
        
        #caida
        if Card.getValue(card) == Card.getValue(self.lastCard):
                print("CAIDA")
                self.playerTurn.score += 2
                self.lastCard = None
                isCaida = True
        for c in orderedCards: 
        #fix llevada function and fix the last card after a cycle        
            if Card.getValue(c) == cardValue:
                self.playerTurn.listSavedCards.append(c)
                self.listCards.remove(c)
                cardValue += 1
                isLlevada = True
        if isCaida or isLlevada :
            self.playerTurn.listSavedCards.append(card)
        else:
            self.lastCard = card
            self.listCards.append(card)

    def checkWinner(self):
        for player in self.playersList:
            if player.score == 40:
                print(".............YOU WIN..........!!!")
                print(f'NUM: {player.playerNumber}')
                print(f'PLAYER: {player.name}')
                print(f'SCORE: {player.score}')
                return True
        return False

    def countCards(self):
        print("<<<<<<<<<<< SHOW INFORMATION >>>>>>>>>>>")
        for player in self.playersList:
            savedCards = len(player.listSavedCards)

            print(f'NUM: {player.playerNumber}')
            print(f'PLAYER: {player.name}')
            print(f'SCORE: {player.score}')
            print(f'CARDS #: {savedCards}')
            if(savedCards >= 20) and player.score < 30:
                points = (savedCards - 20) + 6
                if (points % 2) == 1:
                    points += 1
                player.score += points
                print(f'POINTS ADDED #:{points}')
                print(f'NEW SCORE: {player.score}')
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")