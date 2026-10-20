class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)

        # two = n 
        # one = n-1

        # for i in range(n-1):
        #     temp = 
        #     one = list[one-1]
        #     two = temp
        
        # return one

        #Base Case is 5::::

        # for i in range(len(cost) - 3, -1, -1):
        #     cost[i] += min(cost[i + 1], cost[i + 2])

        # return min(cost[0], cost[1])


        #Base case is 0::::

        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])

        return min(cost[-1], cost[-2])

        #O(n) time
        #O(1) space

