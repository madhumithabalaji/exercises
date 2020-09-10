# -*- coding: utf-8 -*-
inputList = list(input("Enter Queue: "))
del inputList[1:len(inputList):2] #remove blanks
indexList = [index+1 for index, char in enumerate(inputList) if char == '1']
isOk = True 
for i, val in enumerate(indexList):
    if val < len(inputList) and ((indexList[i+1]- indexList[i]) <6):
        isOk = False
        break
print('Safe' if isOk else 'Not Safe')