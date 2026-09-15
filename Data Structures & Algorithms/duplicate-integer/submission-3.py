class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         check = []
         
         for x in nums:
            if x in check:
                return True
            check.append(x)
         return False