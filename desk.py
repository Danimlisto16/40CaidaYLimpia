from icecream import ic
from player import Player

class Desk:
    def __init__(self, listCards,rules,playerTurn,playersList):
        self.listCards = listCards
        self.rules = rules
        self.playerTurn = playerTurn
        self.playersList = playersList
    
    def showDeskCards(self):
        print("========CARDS ON DESK =========")
        print("||                             ||")
        print("||                             ||")
        print(*self.listCards,sep = "\t\n")
        print("||                             ||")
        print("||                             ||")
        print("===============================")    
        print(*self.playersList,sep = "\t\n")
    
        
    def caida(self):
        cardsQtty = len(self.listCards)
        if(cardsQtty > 1):
            if self.listCards[cardsQtty-1].number == self.listCards[cardsQtty-2].number:
                
                    #check if there is any higher card or continue
                
                del(self.listCards[cardsQtty-1])
                del(self.listCards[cardsQtty-2])
                print("==================================")
                print("||             CAIDA            ||")
                print("==================================")
                self.playerTurn.score = self.playerTurn.score + 2
                print(f'\nPlayer: {self.playerTurn.get_name()}  Score: {self.playerTurn.get_score()}')
            
        