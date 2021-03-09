import math
import os
import random
import re
import sys
from itertools import groupby


if __name__ == '__main__':
    s = raw_input()
    alist = {}
    s = sorted(s)
    for key, val in groupby(s):
        alist[key] = len(list(val))
    sorted_keys = sorted(alist, key=alist.get, reverse=True)
    sorted_keys = sorted_keys[:3]
    for key,val in groupby(sorted_keys):
        print(str(key)), 
        print(alist[key])
