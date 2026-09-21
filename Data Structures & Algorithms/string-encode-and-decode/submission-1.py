class Solution:

    def encode(self, strs: List[str]) -> str:
        # MY IDEA was to just use int and not # since we can just skip, but this is not going to work due to multi-digit counter

        # cannot use delimiter flags, because delimiter flag could be part of existing string in strs

        # use data structure to keep track of delimiters? = No cannot output/input more than string

        # beginning of string contains numbers for every space? What if string in strs contains numbers

        # SOLUTION IS DELIMITED WITH COUNT OF WORD. This way if word is "7#hello", you adding delimited WITH counter bypasses the 7# in the string: 7#7#hello....
        # solution = ""

        # map = defaultdict(list)     # key= counter : value = number #WRONG, this fucks up the order that we must preserve.
        # for s in strs:
        #     map[len(s)].append(s) 

        # for k,v in map.items():
        #     solution.append(k+"#"+v)
        
        # return solution

        solution = ""

        for s in strs:
            solution += (str(len(s))+"#"+s)
        
        return solution

    #O(n)
    #O(1) space


    def decode(self, s: str) -> List[str]:
        
        solution = []
        i = 0

        while i < len(s):
            j = i + 1
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            solution.append(s[j+1:j+1+length])
            i = j+length+1
        
        return solution
        
        #O(n)
        #Space: O(1)

        
        # #WRONG = this assumes # is at index 1 which is not always the case for double-digit sized strings
        
        # solution = []
        

        # counter = 0
        # while counter < len(s):
        #     string = range(s[2],s[2+s[counter]],1) 
        #     solution.append(string)
        #     counter = 2+s[counter]

        # return solution
            
            
