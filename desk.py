import time
from icecream import ic
from player import Player


class Desk:
    def __init__(self, listCards,rules,playerTurn,playersList):
        self.__listCards = listCards
        self.__rules = rules
        self.__playerTurn = playerTurn
        self.__playersList = playersList
        
    #getters and setter
    
    def get_listCards(self):
        return self.__listCards
    
    def get_rules(self):
        return self.__rules
    
    def get_playerTurn(self):
        return self.__playerTurn
    
    def get_playersList(self):
        return self.__playersList
    
    #setters
    def set_listCards(self,listCards):
        self.__listCards = listCards
        
    def set_rules(self,rules):
        self.__rules = rules
    
    def set_playerTurn(self,playerTurn):
        self.__playerTurn = playerTurn
    
    def set_playersList(self,playersList):
        self.__playersList = playersList
        
    
    #member functions
    def showDeskCards(self):
        print("========CARDS ON DESK =========")
        print("||                             ||")
        print("||                             ||")
        print(*self.__listCards,sep = "\t\n")
        print("||                             ||")
        print("||                             ||")
        print("===============================")    
        print(*self.__playersList,sep = "\t\n")
    
        
    def caida(self):
        cardsQtty = len(self.__listCards)
        if(cardsQtty > 1):
            if self.__listCards[cardsQtty-1].get_number() == self.__listCards[cardsQtty-2].get_number():
                
                #check if there is any higher card or continuos cards 
                #develop a method that returns a list with all the cards, then add them to the saved cards
                #after, delete them from desk
                print("==================================")
                print("||             CAIDA            ||")
                print("==================================")
                time.sleep(2)
                
                self.__playerTurn.set_score(self.__playerTurn.get_score() + 2)
                
                self.__playerTurn.get_listSavedCards().append(self.__listCards[cardsQtty-1])
                self.__playerTurn.get_listSavedCards().append(self.__listCards[cardsQtty-2])
                
                del(self.__listCards[cardsQtty-1])
                del(self.__listCards[cardsQtty-2])
                
                print(f'\nPlayer: {self.__playerTurn.get_name()}  Score: {self.__playerTurn.get_score()}')
            
        