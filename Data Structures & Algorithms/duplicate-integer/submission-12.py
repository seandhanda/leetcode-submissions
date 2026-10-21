class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {} # value : frequency count 
        
        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        for i in map:
            if map[i] > 1:
                return True
        return False

        #O(n) time
        #O(n) space

