class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # value : index

        for index, num in enumerate(nums):
            lookup = target - num
            if lookup in map:
                return [map[lookup], index]
            else: 
                map[num] = index
        
        #O(n) time
        #O(n) space  
