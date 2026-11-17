class Solution:
    def hammingWeight(self, n: int) -> int:
        # res = 0
        # while n:
        #     if n & 1:
        #         res += 1
        #     n >> 1
        # return res

        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
        



        # res = 0
        # for i in range(32):
        #     if (1 << i) & n:
        #         res += 1
        # return res
        # #O(b) bits
        # #O(1) space

        # res = 0
        # while n:
        #     res += 1 if n & 1 else 0
        #     n >>= 1
        # return res
        # #O(b) time
        # #O(1) space

        # res = 0
        # while n:
        #     n &= n-1   
        #     res += 1
        # return res
        # #O(k) time
        # #O(1) space


        #Max # Bits = 32
        #O(1) time
        #O(1) space
        #FOR ALL 3