import string
with open("Day 5 UNFINISHED\Day 5 input.txt","r") as file:
    D = file.read()
    lines = D.split('\n')

id_,seedsfull = lines[0].split(':')
seeds = [int(seed) for seed in seedsfull.split()]
minseed =  2 ** 63 - 1




for i in range(0,19,2):
    for seed in range(seeds[i],seeds[i+1]):
        changed = False
        for line in lines:
            if line:
                if line[0].isdigit() and not changed:
                    [dstart,sstart,length] = [int(x) for x in line.split()]
                    if seed>sstart and seed<sstart+length:
                        seed=dstart+(seed-sstart)
                        changed = True 
                
                elif line[0] in string.ascii_lowercase:
                    changed = False
        minseed=min(minseed,seed)
print(minseed)

