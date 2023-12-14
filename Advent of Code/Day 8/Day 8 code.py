from collections import defaultdict
from functools import reduce
from math import gcd

with open("Day 8\Day 8 input.txt","r") as file:
    lines = file.read().split('\n')
    maps = lines[2:788]
    directions = lines[0]


def followinstructions(instructions,node):
    for direction in instructions:
        if direction=='R':
            node = mapdict[node][1]
        elif direction=='L':
            node = mapdict[node][0]
    return node


starts=[]
mapdict = dict()
for map in maps:
    node,paths = map.split('=')
    if node.strip().endswith('A'):
        starts+=[node.strip()]
    leftx,rightx = paths.split(',')
    left = leftx.strip()[1:]
    right = rightx.strip()[:-1]
    mapdict[node.strip()] = (left,right)

cyclelength=[]
for start in starts:
    total = 0
    node = start

    while node[-1]!='Z':
        node = followinstructions(directions,node)
        total+=len(directions)
    cyclelength+=[total]

lcm = 1
for i in cyclelength:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)
print(cyclelength)