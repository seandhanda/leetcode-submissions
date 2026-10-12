class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
    #O(1) time
    #O(1) space

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

        #by default this is already in order! = binary search for get()
    #O(1) time
    #O(1) space

    def get(self, key: str, timestamp: int) -> str:
        solution = ""

        if key not in self.map:
            return solution

        left = 0
        right = len(self.map[key])-1


        while left <= right:
            mid = (left + right) // 2
            # if self.map[key][mid][1] == timestamp:
            #     return self.map[key][mid][0]
            value = self.map[key][mid]
            if value[1] <= timestamp:
                left = mid + 1
                solution = value[0]
            elif value[1] > timestamp:
                right = mid -1


        return solution

        #O(logn) where n is the number of entries for key n
        #O(1) space