class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_map = defaultdict(int)
        for c in t: 
            t_map[c] += 1

        s_map = defaultdict(int)
        
        solution = ""

        have = 0
        need = len(t_map)
        
        left = 0
        right = 0

        res = float('inf')

        while right < len(s):
            #VERY IMPORTANT THIS LINE:
            if s[right] in t_map: 
                s_map[s[right]] += 1
            if s[right] in t_map and s_map[s[right]] == t_map[s[right]]:
                have += 1
             

            while have >= need:
                if have == need:
                    if right - left + 1 < res:
                      res = right - left + 1
                      solution = s[left:right+1]

                if s[left] in t_map:
                    s_map[s[left]] -= 1
                if s[left] in t_map and s_map[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1
                
            right += 1

        
            
            
        if res == float('inf'):
            return "" 
        else:
            return solution


    # O(k) space where k is the number of unique characters in s and t, or O(52), or O(1)
    #O(m+n) time