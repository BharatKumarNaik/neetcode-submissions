class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result=0
        i=0
        j=len(heights)-1
        while i<j:
            min_height=min(heights[i],heights[j])
            water_stored=min_height*(j-i)
            # print(water_stored)
            result=max(result,water_stored)
            if heights[i]>heights[j]:
                j-=1
            elif heights[j]>heights[i]:
                i+=1
            else:
                i+=1
        return result