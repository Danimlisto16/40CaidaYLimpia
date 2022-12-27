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
        cardsLen = len(self.playerCards)
        print(f"\nYou have {cardsLen}  card(s)\n")
        while(True):
            try:
                opt = int(input(f"\nPlayer {self.playerNumber}) |{self.name}| choose a card (1-{cardsLen}) : "))
                if opt <= cardsLen and opt >= 1:
                    break
            except:
                print("value exception, please write a number")
        card = Card(self.playerCards[opt-1].symbol,self.playerCards[opt-1].number)
        del(self.playerCards[opt-1])
        return card