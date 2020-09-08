# -*- coding: utf-8 -*-
def seriesSum(n):
    tot = 0
    for i in range(n):
        tot += pow(i+1,i+1)
    res = str(tot)[-10::] #[first:last:-1] for str reverse
    return res;

n = int(input('Input number: '))
print(seriesSum(n))
