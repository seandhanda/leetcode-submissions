class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {} #character : count
        solution = 0
        
        left = 0
        right = 0

        # while right < len(s):
        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) + 1

            windowSize = right - left + 1
            maxFreq = max(seen.values())
            
            while windowSize - maxFreq > k:
                seen[s[left]] -= 1
                left += 1
                windowSize = right - left + 1
                maxFreq = max(seen.values())
            
            # right += 1
            solution = max(solution, windowSize)

        return solution

        #O(mn) = O(n) time
        #O(26) space