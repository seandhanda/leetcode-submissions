class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        freqS = defaultdict(int)
        freqT = defaultdict(int)

        for c in s:
            freqS[c] += 1
        
        for c in t:
            freqT[c] += 1

        return freqS == freqT

        #O(n) time
        #O(n) space                
