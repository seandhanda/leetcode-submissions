class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

        #by default this is already in order! = binary search for get()

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
            index = self.map[key][mid]
            if index[1] <= timestamp:
                left = mid + 1
                solution = index[0]
            elif index[1] > timestamp:
                right = mid -1


        return solution
