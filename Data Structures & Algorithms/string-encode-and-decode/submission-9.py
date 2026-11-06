class Solution:

    def encode(self, strs: List[str]) -> str:
        solution = []

        for i in range(len(strs)):
            solution.append(str(len(strs[i])) + "#" + strs[i])
        
        return "".join(solution)
     
        #O(n) time
        #O(1) space
     
        #     solution = ""

        #     for s in strs:
        #         solution += (str(len(s)) + "#" + s)
        #     return solution

        # #O(n^2) time
        # #O(1) space

    def decode(self, s: str) -> List[str]:
            solution = []

            index = 0

            while index < len(s):
                j = index
                while s[j] != "#":
                    j += 1
                length = int(s[index:j])
                solution.append(s[j+1:j+length+1])
                index = j + length + 1
            
            return solution

            #O(n) time
            #O(1) space


