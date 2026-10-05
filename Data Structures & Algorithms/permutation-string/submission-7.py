from collections import defaultdict
import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #O(n) Approach - Avoid lookup == lookup2 (O(26)) by using matches
        if len(s2) < len(s1):
            return False

        solution = 0 

        lookupS1 = {c:0 for c in string.ascii_lowercase}
        for c in s1:
            lookupS1[c] += 1
    
        left = 0
        right = len(s1)-1
   
        lookupS2 = {c:0 for c in string.ascii_lowercase}
        for i in range(len(s1)):
            lookupS2[s2[i]] += 1 

        matches = 0
        for c in string.ascii_lowercase:
            if lookupS1[c] == lookupS2[c]:
                matches += 1

        while right < len(s2):
            if matches == 26:
                return True
            if lookupS2[s2[left]] == lookupS1[s2[left]]:
                matches -= 1
            lookupS2[s2[left]] -= 1
            if lookupS2[s2[left]] == lookupS1[s2[left]]:
                matches += 1
            left += 1

            right += 1
            if right < len(s2):
                if lookupS2[s2[right]] == lookupS1[s2[right]]:
                    matches -= 1
                lookupS2[s2[right]] += 1
                if lookupS2[s2[right]] == lookupS1[s2[right]]:
                    matches += 1
        
        return False

        #O(n) time
        #O(m+n) space



        # #O(26*n) Approach
        # if len(s1) > len(s2):
        #     return False
        
        # left = 0
        # right = len(s1)-1
        # lookup = defaultdict(int)

        # for c in s1:
        #     lookup[c] += 1

        # lookup2 = defaultdict(int)
        # for i in range(right - left + 1):
        #     lookup2[s2[i]] += 1

        # while right < len(s2):
        #     if lookup2 == lookup:
        #         return True
        #     else:
        #         lookup2[s2[left]] -= 1
        #         if lookup2[s2[left]] == 0:      #Can be avoided by using 26-sized hashmap instead of len(s1)-sized hashmap.
        #             del lookup2[s2[left]]
        #         left += 1
        #         right += 1
        #         if right < len(s2):
        #             lookup2[s2[right]] += 1
        # return False

        # #m is lenth of s1, n is length of s2
        # #O(m+26n) time but since m <= n = O(26*n) time
        # # O(m+n) both bounded by 26 so  = O(1) space

        # #O(min(26, m) space is WRONG! In the case where m is larger than 26, its bounded by 26 = O(1) and when its less than 26, its still O(1) 
 