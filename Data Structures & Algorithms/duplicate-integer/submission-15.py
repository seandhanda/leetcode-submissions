class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # value : frequency count 
        
        for num in nums:
            if num in seen:
                return True
            else: 
                seen.add(num)
        
        return False

        #O(n) time
        #O(n) space

