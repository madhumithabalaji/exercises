    
 #Input: bababadvadv, abcabcbb, pwwkew
 #Problem Statement: https://leetcode.com/problems/longest-substring-without-repeating-characters/
    
class Solution:    
    def subCount(i, ip, count):
        tempCount, tempStr = 1, []
        while i >= -len(ip)+1:
            tempStr.append(ip[i])
            if ip[i] != ip[i-1] and ip[i-1] not in tempStr:
                tempStr.append(ip[i-1])
                tempCount+=1
            elif ip[i] == ip[i-1]:
                tempCount = 1
                tempStr = []
            i-=1
            count.append(tempCount)
            Solution.subCount(i, ip, count)
        return max(count) if len(count) > 0 else 0
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = []
        return Solution.subCount(-1,s,count)

