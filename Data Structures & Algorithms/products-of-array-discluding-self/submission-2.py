class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Optimal = 2 Passes Prefix and Postfix and then one pass calculation all in output 

        solution = [0] * len(nums)
        solution[0] = 1

        for n in range(1,len(nums),+1):
            solution[n] = solution[n-1]*nums[n-1]
        # for n in range(len(nums)-1):
        #     solution[n] *= solution[n+1]*nums[n+1]
        
        postfix = 1
        for n in range(len(nums)-1, -1,-1):
            solution[n] *= postfix
            postfix *= nums[n] 

        return solution

        # O(n)
        #O(1) space



        # #BRUTE FORCE:
        # output = []

        # for i in range(len(nums)):
        #     subsolution = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             subsolution *= nums[j]
        #     output.append(subsolution)
        # return output

        # #O(n^2)
        # # Space: O(n)
