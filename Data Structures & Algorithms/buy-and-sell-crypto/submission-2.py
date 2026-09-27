class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Optimal
        #sliding window
        solution = 0
        
        left = 0
        right = left + 1

        while right <= len(prices)-1:
            profit = prices[right]-prices[left]
            if profit > solution:
                solution = profit

            if prices[right] < prices[left]:
                left =  right
                right += 1
            else: #if right >= left
                right += 1 
        return solution

        #O(n) time
        #O(1) space


        # #brute force iterate n^2 time 
        # solution = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices), +1):
        #         profit = prices[j] - prices[i]
        #         if solution < profit:
        #             solution = profit


        # return solution
