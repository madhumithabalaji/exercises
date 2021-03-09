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
