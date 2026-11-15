class Solution:

    def encode(self, strs: List[str]) -> str:
        solution = []
        for string in strs:
            solution.append(str(len(string)) + "#" + string)
        return "".join(solution)

        #O(n) time
        #O(n) space

    def decode(self, s: str) -> List[str]:
        solution = [] 

        leftIndex = 0

        while leftIndex < len(s):
            rightIndex = leftIndex
            while s[rightIndex] != "#":
                rightIndex += 1
            length = int(s[leftIndex: rightIndex])
            solution.append(s[rightIndex+1 : rightIndex+1 + length])
            leftIndex = rightIndex+1 + length
        
        return solution

        #O(n) time
        #O(1) space
        
            
