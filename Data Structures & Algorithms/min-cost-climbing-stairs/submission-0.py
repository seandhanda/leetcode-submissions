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



        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

        #O(n) time
        #O(1) space

        