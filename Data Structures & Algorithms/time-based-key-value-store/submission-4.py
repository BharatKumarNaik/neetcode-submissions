class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        result = ""
        l,r = 0, len(self.data[key])-1
        # print(self.data[key])
        while l<=r:
            mid = (l+r)//2
            # print(mid)
            if timestamp>=self.data[key][mid][0]:
                result = self.data[key][mid][1]
                l = mid + 1 
            else:
                r = mid - 1
        return result

