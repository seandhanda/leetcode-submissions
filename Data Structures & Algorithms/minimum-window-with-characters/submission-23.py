class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        if len(t) > len(s):
            return ""
        
        count = float('inf')
        solution = ""

        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        sCount = {}

        need = len(tCount)
        have = 0
        
        left = 0
        right = -1

        while right < len(s):
            while have < need:
                right += 1
                if right == len(s):
                    break
                sCount[s[right]] = sCount.get(s[right], 0) + 1
                if s[right] in tCount and sCount[s[right]] == tCount[s[right]]:
                    have += 1

            while have >= need:
                if (right - left + 1) < count:
                    count = right-left+1
                    solution = s[left:right+1]
                sCount[s[left]] -= 1
                if s[left] in tCount and sCount[s[left]] < tCount[s[left]]:
                    have -= 1
                left += 1
        return solution

        #O(n) time
        #O(1) space