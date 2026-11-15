class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {} # number : count
        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        sorted = [[] for _ in range(len(nums)+1)]

        for key in map:
            sorted[map[key]].append(key)
        
        solution = []
        while k:
            for integer in sorted.pop():
                if k == 0:
                    break
                solution.append(integer)
                k -= 1
        return solution

        #O(n) time
        #O(n) space
