class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = max(heights)
        # Bruteforce
        i=0
        for i in range(len(heights)):
            cur = heights[i]
            # prev values parsing to see till what point I can form the rectangle
            prev = i
            while prev>=0 and heights[prev]>=cur:
                prev-=1
            nxt = i
            while nxt<len(heights) and heights[nxt]>=cur:
                nxt+=1
            result = max(result,(nxt-prev-1)*cur)
        return result