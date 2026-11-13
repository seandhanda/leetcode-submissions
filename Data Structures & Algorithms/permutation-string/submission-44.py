class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 and not s2:
            return True
        if not s2 or len(s1) > len(s2):
            return False
    
        # s1Count = {}  #letter : count
        # for c in s1:
        #     s1Count[c] = s1Count.get(c, 0) + 1
        
        # s2Count = {} # letter : count
        # for i in range(0, len(s1)-1):
        #     s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1
        
        s1Count = [0] * 26
        for c in s1:
            s1Count[ord(c) - ord("a")] += 1
        
        s2Count = [0] * 26
        for i in range(len(s1)):
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        left = 0
        right = len(s1) - 1

        while right < len(s2):
            if matches == 26:
                return True
            
            index = ord(s2[left]) - ord("a")
            if s2Count[index] == s1Count[index]:
                matches -= 1
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            left += 1

            right += 1
            if right == len(s2):
                break
            index = ord(s2[right]) - ord("a")
            if s2Count[index] == s1Count[index]:
                matches -= 1
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            
        return False

        #O(n) time
        #O(1) space because O(26)