class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solution = []
        temp = []
        #O(n)
        nums.sort()

        def dfs(index: int) -> None:
            if index > len(nums)-1:
                solution.append(temp.copy())
                return
            
            temp.append(nums[index])
            dfs(index+1)
            temp.pop()

            newIndex = index+1
            while newIndex < len(nums) and nums[newIndex] == nums[index]:
                newIndex += 1
            dfs(newIndex)

        dfs(0)
        return solution

        #O(n * 2^n) time
        #O(n) space