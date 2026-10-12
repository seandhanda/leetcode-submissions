class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        windowSize = len(s1)

        left = 0
        right = len(s1) -1 

        s1_map = defaultdict(int)
        for c in s1:
            s1_map[c] += 1

        s2_map = defaultdict(int)

        matches = 0

        for i in range(right+1):
            if s2[i] in s1_map:
                s2_map[s2[i]] += 1
                if s2_map[s2[i]] == s1_map[s2[i]]:
                    matches += 1

        while right < len(s2):
            if matches >= len(s1_map):
                return True
            
            character = s2[left]
            if character in s1_map:
                if s2_map[character] == s1_map[character]:
                    matches -= 1
                s2_map[character] -= 1
                if s2_map[character] == s1_map[character]:
                    matches += 1
            left += 1

            right += 1 
            if right < len(s2):
                character = s2[right]
                if character in s1_map:
                    if s2_map[character] == s1_map[character]:
                        matches -= 1
                    s2_map[character] += 1
                    if s2_map[character] == s1_map[character]:
                        matches += 1
        return False

        #O(len(s2)) time
        #O(len(s2)) space