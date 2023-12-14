from collections import defaultdict
with open("Day 7\Day 7 input.txt","r") as file:
    lines = file.read().split('\n')

def custom_sort_card(card):
    order = "J23456789TQKA"
    return order.index(card)

def sort_hands(hands):
    return sorted(hands, key=lambda hand: [custom_sort_card(card) for card in hand])


handsdict = {'HCard':[],'Pair1':[],'Pair2':[],'Kind3':[],'FHouse':[],'Kind4':[],'Kind5':[]}
alldict = dict()

for line in lines:
    carddict = defaultdict(int)
    hand, bet = line.split()
    alldict[hand]=int(bet)
    
    Jokers = 0
    for card in hand: 
        if card!='J':
            carddict[card]+=1
        else: Jokers+=1

    
    values = sorted(carddict.values())
    
    if values:
        hi = values[-1]
    else:
        hi = 0
    



    if hi+Jokers==5:
        handsdict["Kind5"]+=[hand]
    
    elif hi+Jokers==4:
        handsdict["Kind4"]+=[hand]

    elif hi+Jokers==3:
        
        if values[-2]==2:
            handsdict["FHouse"]+=[hand]
        
        else: handsdict["Kind3"]+=[hand]
    
    elif hi+Jokers==2:

        if values[-2]==2:
            handsdict["Pair2"]+=[hand]

        else: handsdict["Pair1"]+=[hand]

    else: handsdict["HCard"]+=[hand]

    

for category, values in handsdict.items():
    handsdict[category]= sort_hands(values)

#print(handsdict)



total = 0
index = 1

for category in handsdict.values():
    for hand in category:
        total+=(alldict[hand]*index)
        #print(f"This hand is {hand} and its bet was {alldict[hand]}. It is the {index} best hand. The running total is {total}")
        index+=1
print(total)
    
    
