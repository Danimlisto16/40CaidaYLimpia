from card import Card
from desk import Desk
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
                Card(ks.HEARTS,"6"),
                Card(ks.HEARTS,"5"),
                Card(ks.DIAMONDS,"3"),
                Card(ks.CLUBS,"3"),
                Card(ks.CLUBS,"7")]

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
    playerCards.sort(key = Card.getValue)
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

def checkConsecutives(desk,cardsChoosed):
    isLLevada = False

    if type(cardsChoosed) is list:
        card1 = cardsChoosed[0]
        card2 = cardsChoosed[1]
        card3 = cardsChoosed[2]
        
        desk.playerTurn.listSavedCards.append(card1)
        desk.playerTurn.listSavedCards.append(card2)
        desk.playerTurn.listSavedCards.append(card3)
        
        desk.listCards.remove(card2)
        desk.listCards.remove(card3)
        value1 = Card.getValue(card1) + 1 
    else:
        card1 = cardsChoosed
        value1 = Card.getValue(card1)
            
    orderedCards = desk.orderCards(desk.listCards)
    
    for c in orderedCards: 
        if Card.getValue(c) == value1: #SUM CARDS FOR LLEVADA
            desk.playerTurn.listSavedCards.append(c)
            desk.listCards.remove(c)
            value1 += 1
            isLLevada = True
    return isLLevada

player = Player(1,"JOSE",0,[],[])

desk = Desk([],True,False,player,[player,player],None)

desk.listCards = initialCards.copy()

player.playerCards = playerCards.copy()

#checkRepeatCards(player)

player.showCards()
desk.showDeskCards()

options = player.playerCards
options.extend(showOptions(initialCards,playerCards)) 

print(*options,sep = "\n")

opt = int(input(f'"Which one do you want to take? (1-{len(options)}) : "'))-1

isllevada = checkConsecutives(desk,options[opt])

desk.showDeskCards()

print(player.listSavedCards)

