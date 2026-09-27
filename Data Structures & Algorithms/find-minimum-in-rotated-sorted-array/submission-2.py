class Solution:
    def findMin(self, nums: List[int]) -> int:
        #run binary search and find min, but choose left or right based on new CONDITION (comparing with nums[right])
        # alternatively, you could do the exact same algo, but instead of looking for min, you find pivot (i+1 < i), and then at the end return i - in BOTH algorithms we need a way to decide whether to look left or look right!

        # but i cannot do this, bcause if min < mid, we go to the left, but it might be to the right (for example, when list is: nums = [3,4,5,6,1,2])

        # YOU CANNOT COMPARE WITH nums[left] because of that one special case
        # Must be with nums[right]

        # SPecial Case nums[mid] == nums[right]


        solution = nums[0]

        left = 0 
        right = len(nums)-1


        while left <= right:
            #SPECIAL CASE, OPTIONAL For comparison with nums[right], necessary if comparing with nums[left]
            if nums[left] < nums[right]:
                solution = min(solution, nums[left])
                break 
            # DONE Special Case 
           
            mid = (left + right) // 2
            if nums[mid] < solution:
                solution = nums[mid]
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid - 1

        return solution
        #O(logn) time
        #O(1) space