class Solution:
    def countBits(self, n: int) -> List[int]:
        solution = []
        for i in range(n+1):
            res = 0
            while i:
                if i % 2:
                    res += 1
                i //= 2
            solution.append(res)
        return solution
        #O(nlogn) time
        #O(1) space

