class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #interesting obervation regarding space complexity: heap is O(n) but deque is O(k) because left pointer never stays

        solution = []

        left = 0
        right = k-1

        
        q = deque()

        for i in range(right + 1):
            while q and nums[i] >= q[-1][0]:
                q.pop()
            q.append((nums[i], i))
        
        while right < len(nums):
            solution.append(q[0][0])
            if q[0][1] == left:
                q.popleft()
            right += 1
            left += 1
            if right < len(nums):
                while q and nums[right] >= q[-1][0]:
                    q.pop()
                q.append((nums[right], right))

        return solution

        #O(k) space
        #O(n) time
