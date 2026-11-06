class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # element : frequency 
        sorted = [[] for _ in range(len(nums)+1)] # frequency : element, becuase opposite will require a search for each k

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1
        
        for i in freq:
            sorted[freq[i]].append(i)

        solution  = []
        while k:
            for integer in sorted.pop():
                solution.append(integer)
                k -= 1
                if k == 0:
                    break
        return solution

        #O(n) time
        #O(n) space
        


