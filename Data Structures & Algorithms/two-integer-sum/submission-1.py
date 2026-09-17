class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute force iterate across every index for every index
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        # O(n^2)
        # Space: O(1)
        