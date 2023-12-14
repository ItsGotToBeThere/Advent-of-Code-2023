import math
with open("Day 6\Day 6 input.txt","r") as file:
    lines = file.read().split('\n')
    timeid,timesfull = lines[0].split(':')
    times = [int(time) for time in timesfull.split()]
    distanceid,distancefull = lines[1].split(':')
    distances = [int(distance) for distance in distancefull.split()]

def iseven(num):
    return num%2==0

finaloutput = 1
for i in range(len(times)):
    time = times[i]
    highscore = distances[i]
    total = 0 
    index = 2

    
    if iseven(time):
        total+=1
        middle = time/2
        h=(middle**2)-1
        while (h>highscore):
            total+=2
            h-=index+1
            index+=2


    if not iseven(time):
        middle = math.floor(time/2)
        h = middle*(middle+1)
        while (h>highscore):
            total+=2
            h-=index
            index+=2
    finaloutput*=total
print(finaloutput)



    