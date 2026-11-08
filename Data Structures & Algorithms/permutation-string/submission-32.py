class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 0 and len(s2) == 0:
            return True
        if len(s1) > len(s2):
            return False
        
        s1Count = {} # letter: count
        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1
        
        left = 0
        right = left + len(s1) - 1

        s2Count = {} #letter : count
        for i in range(left, right + 1, 1):
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

        while right < len(s2):
            if s1Count == s2Count:
                return True
            
            s2Count[s2[left]] -= 1
            if s2Count[s2[left]] == 0:
                del s2Count[s2[left]]
            left += 1
            right += 1
            if right == len(s2):
                break
            s2Count[s2[right]] = s2Count.get(s2[right], 0) + 1

        return False 