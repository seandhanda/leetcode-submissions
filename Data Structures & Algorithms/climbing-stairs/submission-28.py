class Solution:
    def climbStairs(self, n: int) -> int:
        #5,4 as base case = Number of ways to get to step 5 from step i
        #0,1 as base case = Number of ways to get to step i

        #5,4 as base case:::::

        #Iterative Space Optimization O(1) using the fact that we only need index+1 and index+2
        

        one = two = 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one

        #O(n) time
        #O(2) = O(1) space



        # # iterative bottom up:
        # dp = [0]*(n+1)

        # dp[n], dp[n-1] = 1, 1
        # for i in range(n-2, -1,-1):
        #     dp[i] = dp[i+1] + dp[i+2]
        # return dp[0]
        
        #O(n) time
        #O(n) space

        #recursive:
        
        # memo = {}
        # memo[n], memo[n-1] = 1,1

        # def dp(index: int) -> int:
        #     if index in memo:
        #         return memo[index]

        #     else:
        #         memo[index] = dp(index+1) + dp(index+2) 
            
        #     return memo[index]

        # return dp(0)


        #O(n) time
        #O(n) space

        #Base Case 0::::

        # #Recursive Top Down
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


        # #Iterative Bottom Up

        # memo = [0] * (n+1)

        # for i in range(n+1):
        #     if i <= 1:
        #         memo[i] = 1
        #     else:
        #         memo[i] = memo[i-2] + memo[i-1]
            
        # return memo[n]
            
        # #O(n) time
        # #O(n) space
