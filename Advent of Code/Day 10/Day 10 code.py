with open ("Day 10\Day 10 test.txt","r") as file:
    lines = file.read().split('\n')
for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char=='S':
            start=[i,j]

def around(index,char):
    nindex = [0,0]
    match char:
        case 'J': nindex = [-1,-1]

