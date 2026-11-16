class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        maxProfit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > maxProfit:
                maxProfit = profit
            if prices[right] < prices[left]:
                left = right
            right += 1
        return maxProfit

        #O(n) time
        #O(1) space