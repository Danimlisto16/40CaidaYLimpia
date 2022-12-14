
class Card:
        
    def __init__(self, symbol, number):
      self.symbol = symbol
      self.number = number
    
    #own methods
    def __str__(self):
        return f'[{self.number} {self.symbol}]'

    def __repr__(self):
        return f'[{self.number} {self.symbol}]'
      
    @staticmethod  
    def getValue(x):
      if x is None:
        return 0
      num = str (x.number)
      try:
        return int(num)
      except:
        if num == 'J':
          return 8
        elif num == 'Q':
          return 9
        else :
          return 10


      