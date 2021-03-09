import sys
from itertools import groupby
input = sys.stdin.readline()

for key, val in groupby(input):
    print(len(list(val)), int(key)),
