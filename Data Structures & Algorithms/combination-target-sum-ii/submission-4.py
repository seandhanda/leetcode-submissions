class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #Set Approach: for each tuple to be added, sort it (because permutation duplicate can occur on different similar indices), and then check if in res set, and add. at the end, return list(set).
        #neetcode uses 3 sum 2 pointer approach.f
        
        res = []

        subset = []

        candidates.sort() #nlogn

        def dfs(index: int, total: int) -> None:
            if total == target:
                res.append(subset.copy())
                return
            if index >= len(candidates):
                return
            if total > target:
                return
            
            subset.append(candidates[index])
            dfs(index+1, total + candidates[index])
            subset.pop()
            
            nextIndex = index + 1
            while nextIndex < len(candidates) and candidates[index] == candidates[nextIndex]:
                nextIndex += 1

            dfs(nextIndex, total)

        
        dfs(0,0)
        return res

        #O(n*2^n) time
        #O(n) space





        # def 2Sum(nums: [], target: int) -> []:
        #     map = defaultdict() # val  :  index
        #     for i in range(len(nums)):
        #         map[nums[i]] = i
            
        #     for i in range(len(nums)):
        #         diff = target - nums[i]
        #         if diff in map:
        #             return [map[diff], i]
        #         else:
        #             map[nums[i]] = i

        #     return
        #     #O(n) time
        #     #O(n) space    


        # #2sum 2 pointer approach
        # def twosum(nums: [], target:int) -> []:  
        #     left = 0
        #     right = len(nums)-1
            


