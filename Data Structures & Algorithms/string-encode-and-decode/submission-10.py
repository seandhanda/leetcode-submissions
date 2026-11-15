class Solution:

    def encode(self, strs: List[str]) -> str:
        solution = []
        for s in strs:
            solution.append(str(len(s)) + "#" + s)
        return "".join(solution)

        #O(n) time
        #O(1) space

    def decode(self, s: str) -> List[str]:
        solution = []
        startIndex = 0
        while startIndex < len(s):
            rightIndex = startIndex
            while s[rightIndex] != "#":
                rightIndex += 1
            length = int(s[startIndex:rightIndex])
            solution.append(s[rightIndex+1:rightIndex+1+length])
            startIndex = rightIndex+1+length
        return solution

        #O(n) time
        #O(1) space

        
            
