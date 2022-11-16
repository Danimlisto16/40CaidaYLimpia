class Player:
    def __init__(self, playerNumber,name, score, playerCards,listSavedCards):
      self.__playerNumber = playerNumber
      self.__name = name
      self.__score = score      
      self.__playerCards = playerCards
      self.__listSavedCards = listSavedCards
 
 #getters
 
    def get_playerNumber(self):
        return self.__playerNumber
    
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
      
    def get_playerCards(self):
        return self.__playerCards
      
    def get_listSavedCards(self):
        return self.__listSavedCards

#setters
    def set_playerNumber(self, a):
        self.__playerNumber = playerNumber
        
    def set_name(self, name):
        self.__name = name
    
    def set_score(self, score):
        self.__score = score
    
    def set_playerCards(self, playerCards):
        self.__playerCards = playerCards
        
    def set_listSavedCards(self,listSavedCards):
        self.__listSavedCards = listSavedCards
        
        
        
        
    def __str__(self):
      return f'|  #{self.playerNumber}) |{self.name}| score: {self.score}'
      