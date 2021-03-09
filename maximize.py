import sys
lines = [x.strip('\n') for x in sys.stdin.readlines()]
lines[0] =[int(x) for x in lines[0].split(" ")]

res = 0
for i in range(1,len(lines)):
    lines[i] = sorted([int(x) for x in lines[i].split(" ")], reverse=True)
    res = res + pow(lines[i][0],2)
tot = res % lines[0][1]
print(tot)
