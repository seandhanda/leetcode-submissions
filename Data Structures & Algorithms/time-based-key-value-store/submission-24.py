class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) #key : [timestamp, value] 

    #O(1) time
    #O(1) space       

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
    
    #O(1) time
    #O(1) space

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        solution = ""
        
        searchArray = self.map[key]
        left = 0
        right = len(searchArray)-1
        while left <= right:
            mid = (left+right)//2
            if searchArray[mid][0] == timestamp:
                return searchArray[mid][1]
            elif searchArray[mid][0] > timestamp:
                right = mid -1
            else:
                solution = searchArray[mid][1]
                left = mid + 1
        return solution
    #O(logn) time where n is the size of searchArray
    #O(1) space




        
