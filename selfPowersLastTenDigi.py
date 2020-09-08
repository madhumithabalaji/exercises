# -*- coding: utf-8 -*-
def seriesSum(n):
    tot = 0
    for i in range(n):
        tot += pow(i+1,i+1)
    res = str(tot)[-10::]
    print(res)
    return True;

n = int(input('Input number?'))
seriesSum(n)
