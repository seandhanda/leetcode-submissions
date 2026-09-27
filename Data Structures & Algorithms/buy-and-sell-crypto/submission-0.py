class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force iterate n^2 time 
        solution = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices), +1):
                profit = prices[j] - prices[i]
                if solution < profit:
                    solution = profit


        return solution