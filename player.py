import time
from card import Card

class Player:
    def __init__(self, playerNumber,name, score, playerCards,listSavedCards):
        self.playerNumber = playerNumber
        self.name = name
        self.score = score      
        self.playerCards = []
        self.listSavedCards = []
        
    def showCards(self):
        iterator = 0
        print("====================")
        print("\n[" + self.name + " CARDS ]")
        for card in self.playerCards:
            iterator = iterator + 1
            print(f'{iterator} ) {card.number} {card.symbol}')
        print("====================")
        
    def __str__(self):
      return f'|  #{self.playerNumber}) |{self.name}| score: {self.score}'


    def chooseCard(self):
        print("==========================================")
        if len(self.playerCards) == 5:
            self.checkRepeatCards()
        cardsLen = len(self.playerCards)
        print(f"\nYou have {cardsLen}  card(s)\n")
        while(True):
            try:
                opt = int(input(f"\nPlayer {self.playerNumber}) |{self.name}| choose a card (1-{cardsLen}) : "))
                if  opt >= 1 and opt <= cardsLen:
                    break
            except:
                print("value exception, please write a number")
        card = Card(self.playerCards[opt-1].symbol,self.playerCards[opt-1].number)
        del(self.playerCards[opt-1])
        print("==========================================")
        return card
        

    
    def checkRepeatCards(self):
        waitSec = 2
        listCards = self.playerCards.copy()
        for _ in range(1,11):
            count = 0
            for c in listCards:
                if Card.getValue(c) == _:
                    count
            if count == 3:
                if self.score < 30:
                    self.score += 2
                    print("<< RONDA >>")
                    time.sleep(waitSec)
                    break
            elif count == 4:
                self.score = 40 
                print("<< POKER >>")
                time.sleep(waitSec)
                break
                    
                    

