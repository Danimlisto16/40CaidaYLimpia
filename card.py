
class Card:
        
    def __init__(self, symbol, number):
      self.__symbol = symbol
      self.__number = number
      
    #getter 
    def get_symbol(self):
        return self.__symbol
    
    def get_number(self):
        return self.__number
      
      #setters
    def set_symbol(self):
          self.__symbol = symbol
          
    def set_number(self):
          self.__number = number
    
    
    #own methods
    def __str__(self):
        return f'[{self.__number} {self.__symbol}]'

    def __repr__(self):
        return f'[{self.__number} {self.__symbol}]'