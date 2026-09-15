class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_map = {}
        for c in t:
            my_map[c] = my_map.get(c, 0) + 1
        

        for c in s:
            if c not in my_map:
                return False
            my_map[c]-=1
            if my_map[c] < 0:
                return False

        return True
