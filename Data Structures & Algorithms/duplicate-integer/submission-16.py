class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #sort = nlogn+n time
        #optimal = n time
        
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
                continue
        
        return False

        #O(n) time
        #O(n) space


