class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        solution = 0
        
        seen = set()

        left = 0
        right = 0

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            solution = max(solution, right-left+1)
            right += 1
            
        return solution

        #O(n) time
        #O(1) space

