from collections import defaultdict


with open("Day 4\Day 4 input.txt","r") as file:
    lines = file.readlines()
N = defaultdict(int)
for k,line in enumerate(lines):
    N[k]+=1
    nums = line.split()
    winningnums = []
    ournums = False
    wins = 0
    for i in range(2,len(nums)):
        if nums[i]=='|': ournums=True
        if not ournums:
            winningnums+=[nums[i]]
        elif ournums:
            if nums[i] in winningnums:
                wins+=1
    print(f"the number of wins of this card is {wins}")
    for j in range(wins):
        N[k+1+j] += N[k]
total = sum(N.values())

    
print(N)  
print(total)