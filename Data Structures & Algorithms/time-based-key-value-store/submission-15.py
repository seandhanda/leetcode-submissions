class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) #key : value (value, timestamp)
        #O(1) time
        #O(1) space

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        #O(1) time
        #O(1) space

    def get(self, key: str, timestamp: int) -> str:
        solution = (float('-inf'),"")
        
        left = 0
        right = len(self.map[key])-1

        while left <= right:
            mid = (left + right)//2 
            tup = self.map[key][mid]
    
            if tup[0] == timestamp:
                if tup[0] > solution[0]:
                    solution = tup
                left = mid + 1
            elif tup[0] < timestamp:
                if tup[0] > solution[0]:
                    solution = tup
                left = mid + 1
            elif tup[0] > timestamp:
                right = mid - 1

        return solution[1]


        #O(logn) where n is the number of entries for key n
        #O(1) space
