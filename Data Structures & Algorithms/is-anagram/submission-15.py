class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {} # character : count
        tMap = {}

        for c in s:
            sMap[c] = sMap.get(c,0) + 1

        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        
        return sMap == tMap

        #O(n) time
        #O(n) space

