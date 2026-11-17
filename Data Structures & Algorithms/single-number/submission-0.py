class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res ^= num
        
        return res

        #O(n) time
        #O(1) space