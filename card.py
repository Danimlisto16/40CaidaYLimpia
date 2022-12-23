
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
    def getValue(card):
      e = card.get_number()
      e = str (e)
      try:
        return int(e)
      except:
        if e == 'J':
          return 8
        elif e == 'Q':
          return 9
        else:
            return 10