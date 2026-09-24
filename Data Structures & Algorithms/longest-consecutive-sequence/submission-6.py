class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Optimal 
        
        
        # # Brute Force - sort the list, begin at index i, track how many times it increments by 1, repeat everytime it breaks, updating tracker
        # solution = 0

        # sortedNums = sorted(nums)

        # for i in range(len(sortedNums)):
        #     tracker = 1
        #     for j in range(i+1,len(sortedNums),+1):
        #         if sortedNums[j] == sortedNums[i]:
        #             i = j
        #             continue
                
        #         if sortedNums[j] == sortedNums[i]+1:
        #             tracker += 1
        #             i = j
        #             continue
        #         break
        #     if tracker > solution:
        #         solution = tracker

        # return solution
                

        # #O(n^2)
        # #O(n)

        # WRONG!!! No need to do n^2 search after sorting, just do one pass = O(nlogn) running time and also we can use nums, no need to create new sortedNums so that gives = O(1)Space
        if nums == []:
            return 0

        nums.sort()

        solution = 0
        tracker = 1

        for i in range(len(nums)-1):
            j = i+1
            if nums[i] == nums[j]:
                continue
            if nums[j] == nums[i]+1:
                tracker += 1  
            #     continue
            else:
                solution = max(tracker, solution)
                tracker = 1
            # # if nums[j] != nums[i]+1:
            # if tracker > solution:
            #     solution = tracker
            #     # continue
            # tracker = 1
        
        solution = max(solution, tracker)

        return solution

        # # errors: 1) sortedNums = sorted(nums) returns new sorted list, not nums.sort() returns none
        # #error 2: forgot equality case
        # #note: setting i within inner loop, not reset by outer loop