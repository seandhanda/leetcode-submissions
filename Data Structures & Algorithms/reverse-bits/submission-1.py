class Solution:
    def reverseBits(self, n: int) -> int:
        #OPTIMAL:

        #Option 1: string manipulation
        # reverse = []
        # #Error: this turns n into 32 bit leading 0s (unsigned input, so no issue) 
        # n = format(n, '032b')
        # for i in range(len(n)-1, -1, -1):
        #     reverse.append(n[i])
        # return int("".join(reverse), 2)
        #O(32) = O(1) time
        #O(32) = O(1) space

        #OR - bitwise
        res = 0

        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

        #Input and Output int is no-base
