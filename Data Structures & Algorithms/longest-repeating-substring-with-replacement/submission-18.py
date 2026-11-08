class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        windowSize = 0
        seen = {} #letter : count
        maxFreq = 0
        res = 0

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) + 1

            windowSize = right - left + 1
            maxFreq = max(seen.values())            

            while (windowSize - maxFreq) > k:
                seen[s[left]] -= 1
                left += 1
                windowSize -= 1
                maxFreq = max(seen.values())


            res = max(res, right - left + 1)
            
        return res

        #O(n) time
        #O(26) space