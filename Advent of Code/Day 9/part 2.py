with open("Day 9\Day 9 input.txt","r") as file:
    lines = file.read().split('\n')

def allzero(history):
    start = True
    for num in history:
        start = start and not num
    return start
def extrapolate(history,tree):
    templist = []
    if allzero(history):
        return history
    for i in range(len(history)-1):
        templist+=[history[i+1]-history[i]]
    tree+=[templist]
    return extrapolate(templist,tree)

total = 0
for line in lines:
    nums=[int(num) for num in line.split()]
    linelist=[nums]
    extrapolate(nums,linelist)
    
    for i in range(len(linelist)-1,-2,-1):
        linelist[i-1].insert(0,linelist[i-1][0]-linelist[i][0])
    total+=linelist[0][0]
print(total)
