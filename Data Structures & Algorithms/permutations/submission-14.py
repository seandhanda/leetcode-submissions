class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution = []
        entry = []
        freq = set()  # integer value : count
        

        def dfs(index: int) -> None:
            if len(entry) == len(nums):
                solution.append(entry.copy())
                return
            if index > len(nums)-1:
                return
            
            dfs(index+1)
            if nums[index] not in freq:
                entry.append(nums[index])
                freq.add(nums[index])
                dfs(0)
                entry.pop()
                freq.remove(nums[index])
            

        dfs(0)
        return solution

        #O(n* _ ) time
        #O(_) space