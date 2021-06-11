#https://www.interviewbit.com/problems/find-duplicate-in-array/
ip = [1,2,3,4,5,8,2,2,4,5,3,4,8,9]
for i in range(1,len(ip)):
    if i - ip.index(ip[i]) > 0 :
        print(ip[i])
        break
