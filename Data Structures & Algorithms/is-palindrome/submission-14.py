class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        #NO, this creates O(n) space
        # sLower = s.lower()

        def alphanum(c: str) -> bool:
            return (ord("A") <= ord(c) <= ord("Z") or
                    ord("a") <= ord(c) <= ord("z") or
                    ord("0") <= ord(c) <= ord("9"))

        while left < right:
            if not alphanum(s[left]):
                left += 1
                continue
            elif not alphanum(s[right]):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        
        return True

        #O(n) time
        #O(1) space
            