class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        freqS = {}
        for c in s:
            freqS[c] = freqS.get(c, 0) + 1
        
        for c in t:
            if c not in freqS or freqS[c] == 0:
                return False
            else:
                freqS[c] -= 1
        return True

        #O(n) time
        #O(n) space

        # if len(t) != len(s):
        #     return False
        
        # freqS = defaultdict(int)
        # freqT = defaultdict(int)

        # for c in s:
        #     freqS[c] += 1
        
        # for c in t:
        #     freqT[c] += 1

        # return freqS == freqT

        # #O(n) time
        # #O(n) space                
