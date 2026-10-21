class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #valid Anagram O(n)
        #compare this with n other str
        #repeat n times
        # = n^3 time 

        # optimal uses one hash map across all strings with value as the string, return this list

        map = {} #tuple : str in strs
 

        for s in strs:
            count = [0] * 26

            for c in s:
                #use 26 becuase otherwise you would need to sort each s before creating its tuple = n^2 total runtime instead of nk runtime    
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key in map:
                map[key].append(s)
            else:
                map[key] = [s]


        return list(map.values())                

        #O(n*k) time where k is max length of all s in strs
        #O(n*k) space

