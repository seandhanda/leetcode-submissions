class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Optimal Cleaner 
        solution = 0 
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            solution = max(solution, right - left + 1)


        return solution
        



        # O(n) time
        # O(1) space



        
        # # Optimal:
        # solution = 0

        # left = 0
        # right = left + 1

        # if not s:
        #     return 0 

        # seen = {s[0]:left}

        # counter = 1
        # while right < len(s):
        #     if s[right] not in seen:
        #         counter += 1
        #         seen[s[right]] = right
        #         right += 1
        #     else:
        #         if counter > solution:
        #                 solution = counter
                
        #         for i in range(left, seen[s[right]],+1):
        #            del seen[s[i]]
        #         left = seen[s[right]] + 1
        #         seen[s[right]] = right
        #         right += 1

        #         counter = right - left

                    
            
        # return max(solution, counter)
        # #O(n)
        # #O(n) space

        # #brute force double loop
        # solution = 0
        # for i in range(len(s)):
        #     seen = set(s[i])
        #     counter = 1
        #     for j in range(i+1,len(s),+1):
        #         if s[j] not in seen:
        #             counter += 1
        #             seen.add(s[j])
        #             continue
        #         else:
        #             break
        #     if counter > solution:
        #         solution = counter
        # return solution
        # #O(n^2)
        # #O(1) space
