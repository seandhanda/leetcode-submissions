class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        my_map = {}
        for c in t:
            my_map[c] = my_map.get(c, 0) + 1
        

        for c in s:
            if c not in my_map:
                return False
            my_map[c]-=1
        
        for key in my_map:
            if my_map[key]!=0:
                return False

        return True
