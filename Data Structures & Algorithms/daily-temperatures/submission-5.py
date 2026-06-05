class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = len(temperatures) - 2
        result = [0] * len(temperatures)
        while i>=0:
            j = i+1
            while temperatures[j]<=temperatures[i]:
                if result[j] == 0:
                    j=len(temperatures)+1
                    # just to know if it didn't find it
                    break
                j+=result[j]
                # directly jump to the point where the next point has higher val then current j
                # which avoids iterating min elements
            if j>=len(temperatures):
                # means j didn't find any max element
                result[i] = 0
            else:
                # j is found the max element
                result[i] = j - i

            i-=1
        return result