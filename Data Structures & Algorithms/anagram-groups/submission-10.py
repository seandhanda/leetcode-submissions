class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Optimal:hash map frequence key : value is the group anagram
        solution = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                # not .get, because key is not a key (yet), its just a list.
                key[ord(c) - ord("a")] += 1
            solution[tuple(key)].append(s)

        return list(solution.values())

        #O(n*m)
        # Space: O(n)

        #Rule 1, cannot do .get(c,0) because key is not a map, its a list and so we must ensure all 26 exist in key= [0] *26 above
        #Rule 2, cannot do solution[tuple(key)] = solution.get(tuple(key), []).append because append will not return, instead we must turn dict into defaultdict(list) so new keys like soltuion[tuple(key)] will default be created as empty list then .append(s)
        #Rule 3: Map Key cannot be list, ue tuple(list)

        
        #Brute Force: Iterate across every string running valid anagram, keeping track of ungrouped strings (ignore all grouped strings)
        # solution = []
        # ungrouped = strs.copy()

        # for i in range(len(strs)):
        #     if strs[i] not in ungrouped:
        #         continue
        #     ungrouped.remove(strs[i])
        #     anagramGroup = [strs[i]]
        #     for j in range(i+1, len(strs)):
        #         map = {}
        #         isAnagram = True
        #         if strs[j] in ungrouped:
        #             if len(strs[i]) != len(strs[j]):
        #                 continue
        #             for c in strs[j]:
        #                 map[c] = map.get(c,0)+1
        #             for c in strs[i]:
        #                 if c not in map:
        #                     isAnagram = False
        #                     break
        #                 map[c] -= 1
        #                 if map[c] < 0:
        #                     isAnagram = False
        #                     break
        #             if not isAnagram:
        #                 continue
        #             ungrouped.remove(strs[j])
        #             anagramGroup.append(strs[j])
        #     solution.append(anagramGroup)   

        # return solution