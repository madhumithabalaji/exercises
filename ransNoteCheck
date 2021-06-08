def countWords(strList):
    dicObj = {item.lower(): strList.count(item.lower()) for item in strList}
    return dicObj

def checkMagazine(magazine, note):
    count, magObj, noteObj = 0, countWords(magazine), countWords(note)
    for key,item in noteObj.items():
        if key in magObj.keys() and item == magObj[key]:
            count+=1
        else:
            break
    print("Yes" if count == len(note) else "No")
    
    #Entry
    magazine, note = ['give', 'me', 'one', 'grand', 'today', 'night'], ['give', 'one', 'grand', 'today']
    checkMagazine(magazine, note)
