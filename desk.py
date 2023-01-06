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
    def __init__(self, listCards,ruleAll2,ruleCardsTill30,playerTurn,playersList,lastCard):
        self.listCards = []
        self.ruleAll2 = ruleAll2
        self.ruleCardsTill30 = ruleCardsTill30
        self.playerTurn = playerTurn
        self.playersList = []
        self.lastCard = lastCard
        
    #member functions
    def showDeskCards(self):
        print("========CARDS ON DESK =========")
        print("||                             ||")
        print("||                             ||")
        print(self.listCards,sep = "\t")
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
        waitSec = 1
        orderedCards = self.orderCards(self.listCards)
        #caida
        if Card.getValue(card) == Card.getValue(self.lastCard):
                print("<||> CAIDA <||>")
                self.playerTurn.score += 2
                self.lastCard = None
                isCaida = True
                time.sleep(waitSec)
        for c in orderedCards: 
        #fix llevada function and fix the last card after a cycle        
            if Card.getValue(c) == cardValue:
                self.playerTurn.listSavedCards.append(c)
                self.listCards.remove(c)
                cardValue += 1
                isLlevada = True
        if isCaida or isLlevada :
            self.playerTurn.listSavedCards.append(card)
            #condition for evaluate LIMPIA
            if (len(self.listCards) == 0) and not self.ruleAll2 :
                print("<||> LIMPIA <||>")
                self.playerTurn.score +=2
                time.sleep(waitSec)
        else:
            self.lastCard = card
            self.listCards.append(card)

    def checkWinner(self):
        for player in self.playersList:
            if player.score >= 40:
                #*********************CHANGE FOR A PRINT PLAYER INFOR
                print(".............YOU WIN..........!!!")
                print(f'NUM: {player.playerNumber}')
                print(f'PLAYER: {player.name}')
                print(f'SCORE: {player.score}')
                print('................................')
                return True
        return False

    def countCards(self):
        print("^^^^^^^^^^^^^ SHOW INFORMATION ^^^^^^^^^^^^^^^^^")
        for player in self.playersList:
            savedCards = len(player.listSavedCards)

# D*********************CHANGE FOR A PRINT PLAYER INFOR
            print(f'NUM: {player.playerNumber}')
            print(f'PLAYER: {player.name}')
            print(f'SCORE: {player.score}')
            print(f'CARDS #: {savedCards}')

            if(savedCards >= 20): #FIX
                points = (savedCards - 20) + 6
                if (points % 2) == 1:
                        points += 1
            # D*********************CHANGE FOR A PRINT PLAYER INFOR
            

                if self.ruleCardsTill30 and player.score < 30:  

                    player.score += points
                    print(f'POINTS ADDED #:{points}')
                    print(f'NEW SCORE: {player.score}')

                elif not self.ruleCardsTill30:
                    player.score += points
                    print(f'POINTS ADDED #:{points}')
                    print(f'NEW SCORE: {player.score}')
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        self.checkWinner()