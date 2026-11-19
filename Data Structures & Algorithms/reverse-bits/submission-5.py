class Solution:
    def reverseBits(self, n: int) -> int:
        #COMPLEXITY ANALYSIS:
        #If 32 Bit max
        # O(1) tima nd space
        #If n bit max AND n represents # of bits
        #O(n) time and space
        # If n bit max and n represents decimal
        #O(logn) time and space

        #OPTIMAL:

        #Option 1: string manipulation
        # reverse = []
        # #Error: this turns n into 32 bit leading 0s (unsigned input, so no issue) 
        #str(n) represents n as "base-10", instead we need:
        # n = format(n, '032b')

        # for i in range(len(n)-1, -1, -1):
        #     reverse.append(n[i])
        # return int("".join(reverse), 2)
        #O(32) = O(1) time
        #O(32) = O(1) space

        #OR - bitwise
        res = 0

        # WRONG: while n:
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
        #O(1) time
        #O(1) space

        #Input and Output int is no-base


        # OPtion 3 = Option 1 string but with reverse = string type instead of list type - THIS IS GENERALLY BAD DUE TO STRING CONCATENATION CREATING O(n^2) time instead of #O(n) time
        # reverse = ""
        # n = format(n, '032b')

        # for i in range(len(n)-1, -1, -1):
        #     reverse += n[i]
        # return int(reverse,2)
        #No 32 bit max - n is number of bits
        #O(n^2) time 
        #O(n) space
       
