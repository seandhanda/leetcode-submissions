class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = defaultdict(list)      # freq : value

        
        for i in range(len(strs)):
            temp = [0] * 26
            for c in strs[i]:
                temp[ord(c)-ord("a")] += 1
            solution[tuple(temp)].append(strs[i])
        return list(solution.values())

        #O(n) time
        #O(n*k) space    

        # #brute force
        # solution = []
        # temp = []
        # seen = set()

        # def validAnagram(i: int, j: int) -> bool:
        #     if len(strs[i]) != len(strs[j]):
        #         return False
            
        #     freqI = {}
        #     for c in strs[i]:
        #         freqI[c] = freqI.get(c, 0) + 1
            
        #     for c in strs[j]:
        #         if c not in freqI or freqI[c] < 1:
        #             return False
        #         else:
        #             freqI[c] -= 1
        #     return True


        # for i in range(len(strs)):
        #     if i in seen:
        #         continue
        #     temp.append(strs[i])
        #     seen.add(i)
        #     for j in range(i+1,len(strs),1):
        #         if j in seen:
        #             continue
        #         if validAnagram(i, j):
        #             temp.append(strs[j])
        #             seen.add(j)
        #     solution.append(temp)
        #     temp = []
    
        # return solution
        

        # #O(n^3) time
        # #O(n) space

                    