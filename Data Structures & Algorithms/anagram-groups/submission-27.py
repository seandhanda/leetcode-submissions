class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list) # [26] : strs
        
        for s in strs:
            entry = [0] * 26
            for c in s:
                entry[ord(c) - ord("a")] += 1
            map[tuple(entry)].append(s)
        return list(map.values())

        #O(n*k) time where n is number of strings and k is max string length
        #O(n) space