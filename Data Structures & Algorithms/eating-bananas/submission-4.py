class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        solution = float('inf')

        while left <= right:
            mid = (left + right) // 2

            hours = 0
            for i in range(len(piles)):
                hours = hours + math.ceil(piles[i]/mid)
            if hours <= h:
                solution = mid
                right = mid - 1
            elif hours > h:
                left = mid + 1
        return solution

        #O(n + log(max(piles))) time
        #O(1) space
