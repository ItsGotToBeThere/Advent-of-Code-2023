with open("Day 4\Day 4 input.txt","r") as file:
    lines = file.readlines()
total = 0
for line in lines:
    nums = line.split()
    winningnums = []
    ournums = False
    n = 0
    for i in range(2,len(nums)):
        if nums[i]=='|': ournums=True
        if not ournums:
            winningnums+=[nums[i]]
        elif ournums:
            if nums[i] in winningnums:
                n+=1
    if n>0:
        win = 2**(n-1)
        total+=win
    
print(total)