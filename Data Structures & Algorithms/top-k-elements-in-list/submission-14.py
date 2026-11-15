class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {} # value : count
        sorted = [[] for _ in range(len(nums)+1)]


        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        for key in map:
            sorted[map[key]].append(key)

        solution = []
        while k:
            for integer in sorted.pop():
                solution.append(integer)
                k -= 1

        return solution
        #O(n) time
        #O(n + k) space


