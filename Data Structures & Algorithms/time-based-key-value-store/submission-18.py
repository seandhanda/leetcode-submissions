class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) # key : [(timestamp, value)]
    
        #O(1) time
        #O(1) space


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

        #O(1) time
        #O(1) space

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        else:
            largestTimestamp = float('-inf')
            solution = ""

            search = self.map[key]
            left = 0
            right = len(search) - 1

            while left <= right:
                mid = (left+right) // 2
                if search[mid][0] <= timestamp:
                    if search[mid][0] > largestTimestamp:
                        largestTimestamp = search[mid][0]
                        solution = search[mid][1] 
                    left = mid + 1
                else:
                    right = mid - 1
        
        return solution

        #O(log(lengh of map[key])) time
        #O(1) space

        
