class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Initial (set usage) = O(n) time and O(n) space

        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            else:
                seen.add(nums[i])
        
        