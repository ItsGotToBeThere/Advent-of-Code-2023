chardict = {'r':0,'g':1,'b':2}
with open("Day 2\Day 2 input.txt","r") as file:
    pulls = file.read()
index = 0
total = 0
array=[0,0,0]
Gameworks = True
for i,char in enumerate(pulls):
    
    if char.isdigit() and pulls[i+3] in chardict.keys() and not pulls[i+2] in chardict.keys(): array[chardict[pulls[i+3]]]+=10*int(char)
    if char.isdigit() and pulls[i+2] in chardict.keys(): array[chardict[pulls[i+2]]]+=int(char)

    if char==";" or char=='G':
        Gameworks = Gameworks and (array[0]<=12 and array[1]<=13 and array[2]<=14)
        print(Gameworks)
        array=[0,0,0]
    if char == 'G':
        if Gameworks: total+=index
        print("The %i Game is %s" % (index,str(Gameworks)))
        print("The running total is %i" % total)
        index+=1
        Gameworks = True
print(total)

    