with open("Day 3\Day 3 input.txt","r") as file:
    lines = file.readlines()
symbols = ['*','$','!','@','#','%','^','&','+','-','=','/']
visitedmap = [[0] * 140 for _ in range(140)]

def num(i,j,lines,visitedmap):
    line=lines[i]
    leftpointer = j-1
    rightpointer = j+1
    while leftpointer>=0 and line[leftpointer].isdigit():
        visitedmap[i][leftpointer] = 1
        leftpointer-=1
         
    while rightpointer<len(line) and line[rightpointer].isdigit():
        visitedmap[i][rightpointer] = 1
        rightpointer+=1
         
    print(line[leftpointer+1:rightpointer])
    return int(line[leftpointer+1:rightpointer])


def around(i,j,lines):
    sum = 0
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if (lines[x][y].isdigit() and not visitedmap[x][y]):
                sum+=num(x,y,lines,visitedmap)
    return sum



def search(lines):
    total = 0
    for i,line in enumerate(lines):
        for j,char in enumerate(line):
            if char in symbols:
                total+=around(i,j,lines)
    return total

print(search(lines))


