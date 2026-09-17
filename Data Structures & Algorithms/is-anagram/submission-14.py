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

        # 2 HASHMAPS = same runtime, same spacetime
        # if len(s) != len(t):
        #     return False

        # s_hashmap = {}
        # t_hashmap = {}

        # Could be same as previous solution, but this one builds both hashmaps in the same loop, hence i in range(len(s)), because c might not be the same across both strings.
        #  for i in range(len(s)):
        #     s_hashmap[s[i]] = s_hashmap.get(s[i],0)+1
        #     t_hashmap[t[i]] = t_hashmap.get(t[i],0)+1

        # if s_hashmap != t_hashmap:
        #     return False
        
        # return True