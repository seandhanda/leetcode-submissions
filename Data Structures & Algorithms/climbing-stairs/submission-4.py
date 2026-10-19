class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
        
        def dp(stair: int) -> int:
            if stair <= 1:
                return 1

            if stair in memo:
                return memo[stair]
            
            memo[stair] = dp(stair-2) + dp(stair - 1)

            return memo[stair]

        return dp(n)

        #O(n) time
        #O(n) space


