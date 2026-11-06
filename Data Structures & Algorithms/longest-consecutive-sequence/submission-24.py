class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force n logn time

        # optimal:
        numsSet = set(nums)

        solution = 0

        for num in numsSet:
            if num-1 in numsSet:
                continue
            else:
                temp = 0
                while num+temp in numsSet:
                    temp += 1
                if temp > solution:
                    solution = temp
        
        return solution

        #O(n) time
        #O(n) space
                    



        
