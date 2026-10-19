class Solution:
    def climbStairs(self, n: int) -> int:
        
        #Recursive Top Down
        # memo = defaultdict(int)
        
        # def dp(stair: int) -> int:
        #     if stair <= 1:
        #         return 1

        #     if stair in memo:
        #         return memo[stair]
            
        #     memo[stair] = dp(stair-2) + dp(stair - 1)

        #     return memo[stair]

        # return dp(n)

        # #O(n) time
        # #O(n) space


        #Iterative Bottom Up

        memo = [0] * (n+1)

        for i in range(n+1):
            if i <= 1:
                memo[i] = 1
            else:
                memo[i] = memo[i-2] + memo[i-1]
            
        return memo[n]
            
