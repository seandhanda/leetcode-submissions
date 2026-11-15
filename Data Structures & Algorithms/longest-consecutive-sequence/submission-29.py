class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        solution = 0

        for num in numsSet:
            if num-1 in numsSet:
                continue
            else:
                count = 1
                while num+1 in numsSet:
                    count += 1
                    num += 1
                if count > solution:
                    solution = count
        return solution
        #O(n) time
        #O(n) space        