class Solution:
    def isAnagram(self, s: str, t:str)-> bool:
        s = "racecar"
        t = "carrace"
        return sorted(s) == sorted(t)
#this is sorting method where time complexity is O(n log n) due to sorting.
"""
class Solution:
    def isAnagram(self, s:str, t:str)-> bool:
        if len(s)!= len(t):
            return False    
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
#this is counting method where time complexity is O(n) due to single pass through the strings.
"""