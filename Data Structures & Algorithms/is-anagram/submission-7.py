class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #turn both strings to arrays, sort them, compare = nlogn runtime

        s= list(s)
        s.sort()
        t= list(t)
        t.sort()

        if t != s:
            return False

        return True
        