class Solution:
    def climbStairs(self, n: int) -> int:
        dp = defaultdict(int)
        
        def dfs(stair: int) -> int:
            if stair <= 1:
                return 1

            if stair in dp:
                return dp[stair]
            
            dp[stair] = dfs(stair-2) + dfs(stair - 1)

            return dp[stair]

        return dfs(n)

        #O(n) time
        #O(n) space


