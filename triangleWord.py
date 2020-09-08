# -*- coding: utf-8 -*-
def checkTriangleWord(val, n):
    for i in range(n):
        if(0.5*i*(i+1) == val):
            return True
        else:
            continue
    return False

strInput = input('Enter word:')
triVal = 0
n = len(strInput) * 26
for char in strInput:
    triVal += ord(char.lower()) - 96
print(triVal, checkTriangleWord(triVal, n))
