file = open("Day 1\Day 1 input.txt", "r")
lines = file.readlines()
numwordsdic = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
output = 0   

for line in lines:
    nums=[]
    for i,char in enumerate(line):
        if char.isdigit(): nums.append(int(char))
        for num in numwordsdic.keys():
            if line[i:].startswith(num): nums.append((numwordsdic[num]))
    output+=(10*nums[0]+nums[-1])
     
print(output)

        








    