class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Logic: Brute force can be optimized to not iterate across all of j after >target, and if we see the pattern, when iterating across i, we end up skipping more and more to the right
       
        #Optimal
        left = 0
        right = len(numbers)-1
        
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] < target:
                left += 1
                continue
            if numbers[left] + numbers[right] > target:
                right -= 1
                continue
        
        
        #O(n) time
        #O(1) space
        #beats enumerate via spacetime

        







        #not sorted enumerate approach

        # lookupMap = defaultdict(int)

        # for i,n in enumerate(numbers):
        #     lookup = target - n
        #     if lookup in lookupMap:
        #         return [lookupMap[lookup]+1, i+1]
        #     #preserve leftmost index if n is already in Map because it is earlier in numbers list and solution wants leftmost index
        #     if lookup not in lookupMap:
        #         lookupMap[n] = i 

        # O(n) time
        #O(n) space



        # need to consider i+j>target then STOP! 
        # #brute force iterate
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers),+1):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        #         if numbers[i] + numbers[j] > target:
        #             break

        # #O(n^2)
        # #O(1) space


