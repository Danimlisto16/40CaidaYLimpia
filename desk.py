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


    def checkConsecutives(self,cardsChoosed):
        isLLevada = False
        if type(cardsChoosed) is list:
            card1 = cardsChoosed[0]
            card2 = cardsChoosed[1]
            card3 = cardsChoosed[2]

            self.playerTurn.listSavedCards.append(card1)
            self.playerTurn.listSavedCards.append(card2)
            self.playerTurn.listSavedCards.append(card3)

            self.listCards.remove(card2)
            self.listCards.remove(card3)
            value1 = Card.getValue(card1)+ 1 
        else:
            value1 = Card.getValue(cardsChoosed)

        orderedCards = self.orderCards(self.listCards)

        for c in orderedCards: 
            if Card.getValue(c) == value1: #SUM CARDS FOR LLEVADA
                self.playerTurn.listSavedCards.append(c)
                self.listCards.remove(c)
                value1 += 1
                isLLevada = True
        return isLLevada

    def checkCaida(self,card):
        if type(card) != list:
            if Card.getValue(card) == Card.getValue(self.lastCard):
                    print("<||> CAIDA <||>")
                    time.sleep(2)
                    self.playerTurn.score += 2
                    return True
        return False
                


    def event(self,cardsChoosen):
        isCaida = False
        isLlevada = False
        isCaida = self.checkCaida(cardsChoosen)
        isLlevada = self.checkConsecutives(cardsChoosen)
        
        if isCaida or isLlevada :
            cardsOnDesk = len(self.listCards)
            if (cardsOnDesk == 0) and not self.ruleAll2 :
                print("<||> LIMPIA <||>")
                self.lastCard = None
                self.playerTurn.score += 2
                time.sleep(2)
        else:
            self.listCards.append(cardsChoosen)
            self.lastCard = cardsChoosen
            

    def checkWinner(self):
        for player in self.playersList:
            if player.score >= 40:
                #*********************CHANGE FOR A PRINT PLAYER INFOR
                print(".............YOU WIN..........!!!")
                player.showInfo()
                print('................................')
                return True
        return False

    def countCards(self):
        print("^^^^^^^^^^^^^ SHOW INFORMATION ^^^^^^^^^^^^^^^^^")
        for player in self.playersList:
            savedCards = len(player.listSavedCards)
            player.showInfo()
            if(savedCards >= 20): #FIX
                points = (savedCards - 20) + 6
                if (points % 2) == 1:
                        points += 1
                if self.ruleCardsTill30 and player.score < 30:  
                    player.score += points
                elif not self.ruleCardsTill30:
                    player.score += points
                print(f'POINTS ADDED #:{points}')
                print(f'SCORE: {player.score}')
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        self.checkWinner()