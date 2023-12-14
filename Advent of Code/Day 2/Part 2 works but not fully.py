with open("Day 2\Day 2 input.txt","r") as file:
    text = file.read()
chardict = {'r':0,'g':1,'b':2}
index = 1
total = num = 0
array=[0,0,0]

for i,char in enumerate(text):
    
    if char.isdigit() and text[i+3] in chardict.keys() and not text[i+2] in chardict.keys(): num+=10*int(char)
    if char.isdigit() and text[i+2] in chardict.keys(): 
        num+=int(char)
        array[chardict[text[i+2]]]=max(array[chardict[text[i+2]]],num)
        num=0

    if (index==100):
        for j in range(len(array)):
            if array[j]==0:
                array[j]=1
        power = array[0]*array[1]*array[2]
        print("game " + str(index))
        print(array)
        print(power)
        total+=power
        array=[0,0,0]
        index+=1
    if char=='\n':
        for j in range(len(array)):
            if array[j]==0:
                array[j]=1
        power = array[0]*array[1]*array[2]
        print("game " + str(index))
        print(array)
        print(power)
        total+=power
        array=[0,0,0]
        index+=1

print(total)
        