class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == len(s2) == 0:
            return True
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26 #letter : value
        for c in s1:
            index = ord(c) - ord("a")
            s1Count[index] += 1
        
        s2Count = [0] * 26
        for i in range(len(s1)):
            index = ord(s2[i]) - ord("a")
            s2Count[index] += 1

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
        #O(1) space
        