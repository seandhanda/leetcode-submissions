class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {} # value : index
        
        for i in range(len(nums)):
            lookupValue = target - nums[i]
            if lookupValue in lookup:
                return [lookup[lookupValue], i]
            else:
                lookup[nums[i]] = i
        
        #O(n) time
        #O(n) space