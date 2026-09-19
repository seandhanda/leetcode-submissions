class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  Brute Force - hashmap frequency for every int in nums, convert hashmap to list of key,value pairs, sort by values, pick top k
        map = {}
        
        for n in nums:
            map[n] = map.get(n, 0) + 1
        
        # list = list(map.items())
        # requires lambda function in sort

        list = []
        for key in map:
            list.append([map[key], key])          # map = freq : int key

        list.sort(reverse = True)

        solution = []
        
        for i in range(k):
            solution.append(list[i][1])

        return solution

        #O(n+n+nlogn+k) = O (nlogn + k) = O(nlogn) K CANNOT EXCEED N (EVEN WHEN ALL N ARE UNIQUE ELEMENTS!!!!!!!!!!!!)
        # Space = O(n+n) = O(n)

