class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        solution = 0 
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            solution = max(solution, right - left + 1)

        return solution
        #O(n) itme
        #O(1) space