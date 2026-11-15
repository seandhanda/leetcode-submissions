class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        solution = 0
        
        numsSet = set(nums)
        for num in nums:
            count = 1
            if num-1 in numsSet:
                continue
            else: 
                while num+1 in numsSet:
                    count += 1
                    num += 1
                if count > solution:
                    solution = count
        return solution 

        #O(n) time
        #O(n) space
                

            
# for num in numsSet
# do I even need line 5