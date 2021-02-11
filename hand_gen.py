import random
import sqlite3


deck = [
'1 Ace hearts','2 Two hearts','3 Three hearts','4 Four hearts','5 Five hearts','6 Six hearts',
'7 Seven hearts','8 Eight hearts','9 Nine hearts','10 Ten hearts','11 Jack hearts',
'12 Queen hearts','13 King hearts',
'1 Ace spades','2 Two spades','3 Three spades','4 Four spades','5 Five spades','6 Six spades',
'7 Seven spades','8 Eight spades','9 Nine spades','10 Ten spades','11 Jack spades',
'12 Queen spades','13 King spades',
'1 Ace diamonds','2 Two diamonds','3 Three diamonds','4 Four diamonds','5 Five diamonds','6 Six diamonds',
'7 Seven diamonds','8 Eight diamonds','9 Nine diamonds','10 Ten diamonds','11 Jack diamonds',
'12 Queen diamonds','13 King diamonds',
'1 Ace clubs','2 Two clubs','3 Three clubs','4 Four clubs','5 Five clubs','6 Six clubs',
'7 Seven clubs','8 Eight clubs','9 Nine clubs','10 Ten clubs','11 Jack clubs',
'12 Queen clubs','13 King clubs'
    ]
seq = "A23456789TJQKA"
deck_copy = deck
flushFlag = 0
flagThree = 0
flagTwo = 0
flushSuit = " "
suitDict={"spades":0,"clubs":0,"diamonds":0,"hearts":0}
hand = "High Card"
def randomise():
    #Distributing first hole card to Player
    holeCard1 = random.choice(deck)
    deck.remove(holeCard1)
    holeCard2 = random.choice(deck)
    deck.remove(holeCard2)

    #Creating list of hole cards for each player
    holeCards = [holeCard1.split()[::2],holeCard2.split()[::2]]

    #Displaying Hole cards of Player 1
    #print(holeCards)

    #List of numbers for player 1's hole cards
    holeCardsList_Numbers = [holeCard1.split()[0],holeCard2.split()[0]]
    #print(holeCardsListP1_Numbers)

    #List of suits for player 1's hole cards
    holeCardsList_Suits = [holeCard1.split()[2],holeCard2.split()[2]]
    #print(holeCardsListP1_Suits)

    #Distributing Community cards
    commCard1 = random.choice(deck)
    deck.remove(commCard1)
    commCard2 = random.choice(deck)
    deck.remove(commCard2)
    commCard3 = random.choice(deck)
    deck.remove(commCard3)
    commCard4 = random.choice(deck)
    deck.remove(commCard4)
    commCard5 = random.choice(deck)
    deck.remove(commCard5)


    #Creating list for community cards

    commCardList = [commCard1.split()[::2],commCard2.split()[::2],commCard3.split()[::2],commCard4.split()[::2],commCard5.split()[::2]]
    hand=commCardList
    hand.extend(holeCards)
    return hand

def RoyalFlush(handCards):
    global flushFlag
    global flushSuit
    global hand
    for i in handCards:
        suitDict[i[1]]+=1
    for k,v in suitDict.items():
        if v>=5:
            flushSuit=k
            flushFlag+=1
    l = []
    for i in handCards:
        if i[1] == flushSuit:
            l.append((i[0]))
    if ("Ten" in l and "Queen" in l and "King" in l and "Jack" in l and "Ace" in l) or (10 in l and 11 in l and 12 in l and 1 in l and 13 in l):
        print("Royal Flush of ",flushSuit.title())
        hand = "Royal Flush"
    elif flushFlag == 1:
        StraightFlush(handCards)
    else:
        FourOfAKind(handCards)
def StraightFlush(handCards):
    l=[]
    global hand
    for i in handCards:
        if i[1] == flushSuit:
            l.append(int((i[0])))
    l.sort()
    straightFlush = False
    try:
        for i in range(3):
            if  l[i:i+5]==list(range(l[i],l[i]+5)):
                straightFlush = True
    except:
        pass
    finally:
        if straightFlush:
            hand = "Straight Flush"
            print(f"Straight Flush")
        else:
            FourOfAKind(handCards)
def FourOfAKind(handCards):
    l=[]
    global hand
    for i in handCards:
        if int(i[0])<10:
            l.append(i[0])
        else:
            l.append(seq[int(i[0])-1])
    cardString = "".join(l)
    flag=0
    for i in cardString:
        if cardString.count(i) == 4:
            flag = 1
            break
    if flag == 1:
        print("Four of a kind")
        hand = "Four of a kind"
    else:
        FullHouse(handCards)
def FullHouse(handCards):
    l = []
    global flagThree
    global flagTwo
    global hand
    for i in handCards:
        if int(i[0])<10:
            l.append(i[0])
        else:
            l.append(seq[int(i[0])-1])
    cardString = "".join(l)
    for i in cardString:
        if cardString.count(i)==3:
            flagThree += 1
        elif cardString.count(i)==2:
            flagTwo += 1
    if flagThree == 1 and flagTwo == 2:
        print("Full House")
        hand = "Full House"
    elif flushSuit in suitDict.keys():
        Flush(handCards)
    else:
        Straight(handCards)
def Flush(handCards):
    print("Flush")
    global hand
    hand = "Flush"
def Straight(handCards):
    distinctList = []
    for i in handCards:
        if i in distinctList:
            distinctList.append(i[0])
    distinctList.sort()
    global hand
    try:
        flag = 0
        for i in range(len(distinctList) - 4):
            if distinctList[i:i + 5] == list(range(distinctList[i], distinctList[i] + 5)):
                flag = 1
        if flag == 0:
            ThreeOfAKind(handCards)
        else:
            print("Straight")
            hand = "Straight"
    except:
        ThreeOfAKind(handCards)
def ThreeOfAKind(handCards):
    global flagThree
    global hand
    if flagThree >= 1:
        hand = "Three of a kind"
        print("Three of a kind")
    else:
        TwoPairs(handCards)
def TwoPairs(handCards):
    global flagTwo
    global hand
    if flagTwo/2 >=2:
        hand = "Two pair"
        print("Two pair")
    else:
        OnePair(handCards)
def OnePair(handCards):
    global flagTwo
    global hand
    if flagTwo/2 == 1:
        print("One pair")
        hand = "One pair"
    else:
        HighCard(handCards)
def HighCard(handCards):
    l=[]
    for i in handCards:
        if int(i[0])<10:
            l.append(i[0])
        else:
            l.append(seq[int(i[0])-1])
    l.sort(reverse=True)
    hand = "High Card"
    if 'A' in l:
        print("High Card A", l[0])
    else:
        print("High Card ", l[0])

#hand = hand.lower()
x = randomise()
print(x)
print(hand)