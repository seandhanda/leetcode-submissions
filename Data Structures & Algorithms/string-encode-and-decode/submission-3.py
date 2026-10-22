class Solution:

    def encode(self, strs: List[str]) -> str:
        solution = ""
        for s in strs:
            solution += str(len(s)) + "#" + s
        return solution

        #O(n) time
        #O(1) space

    def decode(self, s: str) -> List[str]:
        solution = []
        index = 0

        while index < len(s):
            j = index
            while s[j] != "#":
                j+=1
            size = int(s[index:j])
            temp = s[(j+1) : ((j+1)+size)]
            solution.append(temp)
            index = ((j+1)+size)
        return solution

        #O(n) time
        #O(k) space