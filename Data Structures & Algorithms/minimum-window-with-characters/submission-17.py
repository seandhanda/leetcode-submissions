class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = float('inf')
        solution = ""

        if len(s) < len(t):
            return ""
        if len(s) == len(t) == 0:
            return ""

        t_map = {} # letter : count
        for c in t:
            t_map[c] = t_map.get(c,0) + 1
        
        s_map = {} # letter : count
        have = 0
        need = len(t_map)

        left = 0
        right = -1

        while right < len(s):
            right += 1
            if right == len(s):
                break
            s_map[s[right]] = s_map.get(s[right], 0) + 1
            if s[right] in t_map and s_map[s[right]] == t_map[s[right]]:
                have += 1    
                
            while have >= need:
                if (right - left + 1) < count:
                    count = right - left + 1
                    solution = s[left:right + 1]
                if s[left] in t_map and s_map[s[left]] == t_map[s[left]]:
                    have -= 1
                s_map[s[left]] -= 1
                left += 1

        return solution

        #O(n) time
        #O(26) = O(1) space