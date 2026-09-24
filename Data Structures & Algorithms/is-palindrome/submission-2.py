class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        
        # left = 0
        # right = len(s)-1

        # while left < right: # if even, this is perfect. if odd, the middle character will always pass palindrome requirement. this works!
        #     if not s[left].isalnum():
        #         left += 1
        #         continue
        #     if not s[right].isalnum():
        #         right -= 1
        #         continue
            
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        
        # return True

        #O(n) time
        #O(1) space

        # but what if interviewer does not want us using built in python library function isalnum()?
        # Then do this!:

        left = 0
        right =  len(s)-1

        while left < right:
            if not self.isalnum(s[left]):
                left += 1
                continue
            if not self.isalnum(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -=1
        return True

    def isalnum(self, c):
        if (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9")):
            return True
        else:
            return False
        
        
        
        #done






        # #another way - ineffieicent because not O(1) space. use 2 pointer instead!!!
        # newString = ""

        # for c in s:
        #     if c.isalnum():
        #         newString += c.lower() 
        
        # if newString == newString[::-1]:
        #     return True
        
        # return False
        