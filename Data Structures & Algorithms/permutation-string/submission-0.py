from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        left = 0
        right = len(s1)-1
        lookup = defaultdict(int)

        for c in s1:
            lookup[c] += 1

        lookup2 = defaultdict(int)
        for i in range(right - left + 1):
            lookup2[s2[i]] += 1

        while right < len(s2):
            if lookup2 == lookup:
                return True
            else:
                lookup2[s2[left]] -= 1
                if lookup2[s2[left]] == 0:
                    del lookup2[s2[left]]
                left += 1
                right += 1
                if right < len(s2):
                    lookup2[s2[right]] += 1
        return False

        #m is lenth of s1, n is length of s2
        # O(1) space
        #O(min(26, m) space WRONG!, O(1). In the case where m is larger than 26, its bounded by 26 = O(1) and when its less than 26, its still O(1) 
        #O(m+n) time
 