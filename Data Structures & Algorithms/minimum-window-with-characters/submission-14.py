class Solution:
    def minWindow(self, s: str, t: str) -> str:
        solution = ""

        if len(t)>len(s):
            return solution

        count = float('inf')
        
        left = 0
        right = -1
        
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        s_map= defaultdict(int)
        have = 0
        need = len(t_map)

        while right < len(s):
            while have < need:
                right += 1    
                if right == len(s): break
                s_map[s[right]] += 1
                if s_map[s[right]] == t_map[s[right]]:
                    have += 1

            while have >= need:
                if right - left < count:
                    solution = s[left:right+1]
                    count  = right - left + 1
                s_map[s[left]] -= 1
                if s_map[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1

        return solution

        #O(n) time
        #O(k) space