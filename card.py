
class Card:
    def __init__(self, symbol, number):
      self.symbol = symbol
      self.number = number
      
    def __str__(self):
        return f'[{self.number} {self.symbol}]'

    def __repr__(self):
        return f'symbol: {self.symbol} number: {self.number}'