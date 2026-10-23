class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]

        one = nums[0]
        two = max(nums[0], nums[1])

        for i in range(2, len(nums),1):
            temp = two
            two = max(two, one+nums[i])
            one = temp
        return two
        #O(n) time
        #O(1) space


































        # one, two = 0,0

        # for num in nums:
        #     temp = two
        #     two = max(two, num+one)
        #     one = temp
        # return two


        # # overwrite
        # if len(nums) == 1:
        #     return nums[0]

        # nums[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     nums[i] = max(nums[i-1], nums[i] + nums[i-2])

        # return nums[-1]

        #O(1) space
        #O(n) time

        # # ITERATIVE
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # if len(nums) > 1:
        #     dp[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums), 1):
        #     dp[i] = max((nums[i] + dp[i-2]), dp[i-1])
        
        # return dp[len(nums)-1]


    #     # RECURSIVE
    #     memo = {}
    #     memo[0] = nums[0]
    #     if len(nums) > 1:
    #         memo[1] = max(nums[0], nums[1])

    #     def dp(index: int) -> int:
    #         if index in memo:
    #             return memo[index]

    #         memo[index] = max(nums[index] + dp(index - 2), dp(index - 1))
    #         return memo[index]

    #     return dp(len(nums) - 1)

    # # O(n) time
    # # O(n) space

