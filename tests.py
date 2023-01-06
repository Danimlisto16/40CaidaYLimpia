from card import Card
from kindSymbol import kindSymbol as ks
from player import Player

initialCards = [
            #HEARTS
            Card(ks.HEARTS,"1"),
            Card(ks.DIAMONDS,"2"),
            Card(ks.SPADES,"3"),
            Card(ks.CLUBS,"4"),
            Card(ks.CLUBS,"5")
            ]

playerCards = [ 
                Card(ks.HEARTS,"3"),
                Card(ks.HEARTS,"5"),
                Card(ks.DIAMONDS,"3"),
                Card(ks.CLUBS,"3"),
                Card(ks.CLUBS,"3")]

def showOptions(deskCards,playerCards):
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
    for opt in playerCards:
        vOpt = Card.getValue(opt)
        for pairs in comb:
            v1 = Card.getValue(pairs[0])
            v2 = Card.getValue(pairs[1]) 
            if (v1 + v2) == vOpt:
                options.append([opt,pairs[0],pairs[1]])
    return options


def checkRepeatCards(player):
        waitSec = 2
        listCards = player.playerCards.copy()
        for _ in range(1,11):
            count = 0
            for c in listCards:
                if Card.getValue(c) == _:
                    count+=1
            if count == 3:
                if player.score < 30:
                    player.score += 2
                    print("<< RONDA >>")
                    break
            elif count == 4:
                player.score = 40 
                print("<< POKER >>")    
                break

player = Player(1,"JOSE",0,[],[])

player.playerCards = playerCards.copy()

checkRepeatCards(player)



#options = showOptions(initialCards,playerCards)
#print(*options,sep = "\n")



