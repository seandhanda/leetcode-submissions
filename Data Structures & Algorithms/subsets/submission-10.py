class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        temp = []

        def dfs(index: int) -> None:
            if index > len(nums)-1:
                solution.append(temp.copy())
                return
            
            temp.append(nums[index])
            dfs(index+1)
            temp.pop()
            dfs(index+1)
            

        dfs(0)
        return solution
        
        #O(n * 2^n) time
        #O(n) space