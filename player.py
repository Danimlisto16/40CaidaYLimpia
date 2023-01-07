import time
from card import Card

class Player:
    def __init__(self, playerNumber,name, score, playerCards,listSavedCards):
        self.playerNumber = playerNumber
        self.name = name
        self.score = score      
        self.playerCards = []
        self.listSavedCards = []


    def __str__(self):
        return f'|  #{self.playerNumber}) |{self.name}| score: {self.score}'


    def showOptions(self, options):
        print("====================")
        ite = 1
        print("\n[" + self.name + " CARDS ]")
        for card in options:
            print(f'{ite} ) {card}')
            ite+=1
        print("====================")
        

    def chooseCard(self, desk): #REFACTOR **************
        cardChoosed = []
        options = self.playerCards
        options.extend(self.generateOptions(desk.listCards))

        self.showOptions(options)

        if len(self.playerCards) == 5:
            self.checkRepeatCards()

        print("==========================================")
        optLen = len(options)            
        print(f"\nYou have options(s)\n")
        while(True):
            try:
                opt = int(input(f"\nPlayer {self.playerNumber})|{self.name}| choose a card (1-{optLen}) : "))
                if  opt >= 1 and opt <= optLen:
                    opt = opt - 1
                    break
            except:
                print("value exception, please write a number")
        cardsChoosed = options[opt]
        options.remove(options[opt])
        print("==========================================")
        return cardsChoosed
        

    def showInfo(self):
        print(f'NUM: {self.playerNumber}')
        print(f'PLAYER: {self.name}')
        print(f'SCORE: {self.score}')
        print(f'CARDS #: {self.listSavedCards}')
    
    def checkRepeatCards(self):
        listCards = self.playerCards.copy()
        for _ in range(1,11):
            count = 0
            for c in listCards:
                if Card.getValue(c) == _:
                    count+=1
            if count == 3:
                if self.score < 30:
                    self.score += 2
                    print("<< RONDA >>")
                    break
            elif count == 4:
                self.score = 40 
                print("<< POKER >>")    
                break          

            
    def generateOptions(self,deskCards):
        playerCards = self.playerCards.copy()
        comb = []
        for card1 in deskCards:
            for card2 in deskCards:
                v1 = Card.getValue(card1)
                v2 = Card.getValue(card2)

                if v1 + v2 <= 7 and  v1 != v2:
                    nOrdered = [card1,card2]
                    nOrdered.sort(key = Card.getValue)
                    if nOrdered not in comb:
                        comb.append(nOrdered)
        options = []
        playerCards.sort(key = Card.getValue)
        for opt in playerCards:
            vOpt = Card.getValue(opt)
            for pairs in comb:
                v1 = Card.getValue(pairs[0])
                v2 = Card.getValue(pairs[1]) 
                if (v1 + v2) == vOpt:
                    options.append([opt,pairs[0],pairs[1]])
        return options