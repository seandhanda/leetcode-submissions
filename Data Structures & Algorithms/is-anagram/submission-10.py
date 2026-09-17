class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_hashmap = {}

        for c in t:
            t_hashmap[c] = t_hashmap.get(c,0)+1
        
        for c in s:
            if c not in t_hashmap:
                return False
            t_hashmap[c] -= 1

            if t_hashmap[c] < 0:
                return False

        return True