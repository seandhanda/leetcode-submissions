class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} #value : count

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        sorted = [[] for i in range(len(nums) + 1)] #+1 HERE     # index = count, value = strings

        for key in freq:
            sorted[freq[key]].append(key)

        solution = []

        while k:
            for integer in sorted.pop():
                solution.append(integer)
                k -= 1
        
        return solution

        #O(n) time
        #O(n) space

