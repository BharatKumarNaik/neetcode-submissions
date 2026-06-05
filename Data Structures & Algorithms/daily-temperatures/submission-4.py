class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = len(temperatures) - 2
        result = [0] * len(temperatures)
        while i>=0:
            j = i + 1
            while temperatures[i]>=temperatures[j] and j<=len(temperatures):
                # print(i,j)
                if result[j] ==0:
                    j = len(temperatures)+1
                    break
                else:
                    j+=result[j]
            if j >= len(temperatures):
                result[i] = 0
            else:
                result[i] = j - i

            i-=1
        return result