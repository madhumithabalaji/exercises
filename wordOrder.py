import sys
lines = [x.strip('\n') for x in sys.stdin.readlines()]
lines.pop(0)
occ = []
for line in lines:
    if (lines.count(line) == 1):
        occ.append(1)
    if(lines.count(line) > 1):
        occ.append(lines.count(line))
        lines.remove(line)

print(len(lines))
print(' '.join(map(str, occ)))

#Another method
import sys
from itertools import groupby
lines = [x.strip('\n') for x in sys.stdin.readlines()]
lines.pop(0)
lines = sorted(lines)
a = []
for key, val in groupby(lines):
    a.append(len(list(val)))
print(len(a)) 
for i in sorted(a, reverse=True):
    print(i),
