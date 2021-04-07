if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    ip = sorted([x for x in arr], reverse = True)
    i, max = 0, ip[0] 
    while True:
        if(ip[i]==max):
            i+=1
        elif (ip[i]<max):
            print(ip[i])
            break
