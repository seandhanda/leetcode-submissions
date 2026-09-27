import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Optimal: same algo, instead of starting from 1, we do binary search on possible k values.        
        left = 1 
        right = max(piles)
        # right = len(piles)-1
        solution = max(piles)
        
        while left <= right:

            k = (left + right) // 2 
            time = 0

            for i in range(len(piles)):
                time += math.ceil(piles[i] / k)

            if time <= h:
                right = k-1
                solution = k
                # if time < solution: #NOT NEEDED, k will always be the same or smaller
                continue

            elif time > h: 
                left = k+1
                continue
        return solution
        #O(1) space
        # O(n * log(m)) time # IT IS NOT logk, k is our solution not the max(piles), use anothe vairable m for this.

        # # brute force, start from 0 and keep trying upwards
        # # if len(piles) > h:
        # #     return False 
        # for k in range(1, max(piles)+1):
        #     hours = 0
        #     for i in range(len(piles)):
        #         hours += math.ceil(piles[i] / k) 
        #     if hours <= h:
        #         return k
        # #O(n * max(piles)) time
        # #O(1) space
            