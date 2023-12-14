from collections import defaultdict
with open("Day 7\Day 7 input.txt","r") as file:
    lines = file.read().split('\n')

def custom_sort_card(card):
    order = "23456789TJQKA"
    return order.index(card)

def sort_hands(hands):
    return sorted(hands, key=lambda hand: [custom_sort_card(card) for card in hand])



handsdict = {'HCard':[],'Pair1':[],'Pair2':[],'Kind3':[],'FHouse':[],'Kind4':[],'Kind5':[]}
alldict = dict()

for line in lines:
    handdict = defaultdict(int)
    hand, bet = line.split()
    alldict[hand]=int(bet)
    
    for card in hand: 
        handdict[card]+=1
    
    handvalues = sorted(handdict.values())
    hi = handvalues[-1]

    if hi==5:
        handsdict["Kind5"]+=[hand]
    
    elif hi==4:
        handsdict["Kind4"]+=[hand]

    elif hi==3:
        
        if handvalues[-2]==2:
            handsdict["FHouse"]+=[hand]
        
        else: handsdict["Kind3"]+=[hand]
    
    elif hi==2:

        if handvalues[-2]==2:
            handsdict["Pair2"]+=[hand]

        else: handsdict["Pair1"]+=[hand]

    else: handsdict["HCard"]+=[hand]

    

for category, values in handsdict.items():
    handsdict[category]= sort_hands(values)

print(handsdict)



total = 0
index = 1

for category in handsdict.values():
    for hand in category:
        total+=(alldict[hand]*index)
        print(f"This hand is {hand} and its bet was {alldict[hand]}. It is the {index} best hand. The running total is {total}")
        index+=1
print(total)
    
    
