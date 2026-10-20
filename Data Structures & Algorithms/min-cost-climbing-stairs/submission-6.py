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

        #Space-Optimized:::::


        #Space Optimized Base Case is 5 but using same template as prev problem: THE REASON WHY SOMETIMES WE USE 2 variables vs array is based on what input we are given!!!!
        # one = two = 0

        # for i in range(len(cost) - 1, -1, -1):
        #     current = cost[i] + min(one, two)
        #     two = one
        #     one = current

        # return min(one, two)

        #O(n) time
        #O(1) space


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




 # WRONG - you are using i so it cant just be iterator, it must be correctly starting at index 2 otherwise i-2 out of bounds for i < 2
        # n = len(cost)
        
        # # for i in range(n-1):
        # #     cost[i] += min(cost[i-1], cost[i-2])

        # # return min(cost[n-1], cost[n-2])
       