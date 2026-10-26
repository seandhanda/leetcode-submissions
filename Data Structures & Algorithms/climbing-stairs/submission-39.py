class Solution:
    def climbStairs(self, n: int) -> int:
        # #stairs from 1 to n, ground is 0, so we want to return dp[n]
        # #iterative

        # #initalizes index 0 to len(cost) -1 = len(cost)-1
        # dp = [0] * (n+1)
        # dp[0] = 1
        # if n >= 1:
        #     dp[1] = 1

        # for i in range(2, n+1,+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]

        # #O(n) time
        # #O(n) space

        # # Recursive
        # memo = defaultdict(int)

        # def dp(index: int) -> int:
        #     if index <= 1:
        #         return 1
            
        #     if index in memo:
        #         return memo[index]

        #     memo[index] = dp(index-1) + dp(index-2)
        #     return memo[index]

        # return dp(n)

        # #O(n) time
        # #O(n) space

        # iterative space optimized:
        
        # if n<=1:
        #     return 1

        one, two = 1, 1

        for i in range(2, n+1):
            temp = two
            two = one + two
            one = temp
        return two
        #O(n) time
        #O(1) space

        