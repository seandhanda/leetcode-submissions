class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # optimal - monotonic decreasing stack

        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            
            while stack and t > stack[-1][0]:
                stackTemperature, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((t,i))
        
        return result
        
        # #brute force is double loop iteration
        # result = [0] * len(temperatures)
        # for i in range(len(temperatures)-1):        
        #     days = 1
        #     j = i+1
        #     while j < len(temperatures) and temperatures[i] >= temperatures[j]:
        #         days += 1
        #         j += 1
        #     if j < len(temperatures):
        #         result[i] = days
        # return result
        # # O(n^2) runtime
        # # O(1) space