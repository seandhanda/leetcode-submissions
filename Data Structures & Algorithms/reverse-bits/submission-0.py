class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = []
        #Error: this turns n into decimal 1000 -> 
        n = format(n, '032b')
        for i in range(len(n)-1, -1, -1):
            reverse.append(n[i])
        return int("".join(reverse), 2)
        #O(n) time
        #O(n) space


        # n is an input represented in binary
    

