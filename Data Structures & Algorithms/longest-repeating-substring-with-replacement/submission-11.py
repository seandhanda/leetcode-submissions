class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        solution = 0

        lookup = {}

        left = 0
        right = 0

        while right <= len(s)-1:
            lookup[s[right]] = lookup.get(s[right],0) + 1
            
            
            
            windowSize = right - left + 1
            #O(26) time:
            # mostFrequent = max(lookup, key = lookup.get)
            mostFrequent = max(lookup.values())

            if windowSize - mostFrequent <= k:
                solution = max(solution, windowSize)
            else:
                while windowSize - mostFrequent > k:
                    lookup[s[left]] -= 1
                    left += 1
                    windowSize -= 1
                    
            right += 1

        return solution

        #O(26*n) = O(n) time
        #O(26)




            