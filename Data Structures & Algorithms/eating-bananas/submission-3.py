class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        minimum = 1
        #O(n) time
        maximum = max(piles)

        solution = maximum

        while minimum <= maximum:
            mid = (minimum+maximum)//2 
            
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i]/mid)
            if time <= h:
                solution = mid
                maximum = mid - 1
            else:
                minimum = mid + 1
        return solution

        #O(n + logm) time
        #O(1) space
            