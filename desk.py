import time
from icecream import ic
from player import Player

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
        self.__listCards = listCards
        self.__rules = rules
        self.__playerTurn = playerTurn
        self.__playersList = playersList
        self.__lastCard = lastCard
    #getters and setter
    
    def get_listCards(self):
        return self.__listCards
    
    def get_rules(self):
        return self.__rules
    
    def get_playerTurn(self):
        return self.__playerTurn
    
    def get_playersList(self):
        return self.__playersList
    
    def get_lastCard(self):
        return self.__lastCard
    
    #setters
    def set_listCards(self,listCards):
        self.__listCards = listCards
        
    def set_rules(self,rules):
        self.__rules = rules
    
    def set_playerTurn(self,playerTurn):
        self.__playerTurn = playerTurn
    
    def set_playersList(self,playersList):
        self.__playersList = playersList
        
    def set_lastCard(self,lastCard):
        self.__lastCard = lastCard
        
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
    
        
    def caida(self,card):
        if len(self.__listCards.get_listCards()) > 0:
            if self.get_lastCard().get_number() == card.get_number():
                self.__playerTurn.set_score(self.__playerTurn.get_score() + 2)        
                self.__playerTurn.get_listSavedCards().append(card)
                self.__playerTurn.get_listSavedCards().append(self.__lastCard)
                self.get_listCards().remove(self.get_lastCard())
                print(f'\nPlayer: {self.__playerTurn.get_name()}  Score: {self.__playerTurn.get_score()}')
                print("==================================")
                print("||             CAIDA            ||")
                print("==================================")
                time.sleep(2)
            else:
                self.__get_listCards().append(card) #when is a list you need to get it and append it    
            