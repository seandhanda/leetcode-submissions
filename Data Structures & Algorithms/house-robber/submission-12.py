class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        memo[0] = nums[0]
        if len(nums) > 1:
            memo[1] = max(nums[0], nums[1])
        
        def dp(index: int) -> int:
            if index in memo:
                return memo[index]
            
            memo[index] = max(nums[index] + dp(index - 2), dp(index-1))
            return memo[index]
        
        return dp(len(nums)-1)    

    #O(n) time
    #O(n) space