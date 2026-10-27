class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # s = s.lower()
        #O(n) time
        
        left = 0
        right = len(s)-1


        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            elif not self.isalphanum(s[right]):
                right -=1
                continue
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True                


    def isalphanum(self, c: str) -> bool:
        if (ord("a") <= ord(c) <= ord("z") or
            ord("A") <= ord(c) <= ord("Z") or
            ord("0") <= ord(c) <= ord("9")):
            return True
        else: 
            return False
    #O(n) time
    #O(1) space
