class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Optimal

        
        #not sorted enumerate approach

        lookupMap = defaultdict(int)

        for i,n in enumerate(numbers):
            lookup = target - n
            if lookup in lookupMap:
                return [lookupMap[lookup]+1, i+1]
            #preserve leftmost index if n is already in Map because it is earlier in numbers list and solution wants leftmost index
            if lookup not in lookupMap:
                lookupMap[n] = i 
        
        # #brute force iterate
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers),+1):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]

        # #O(n^2)
        # #O(1) space


