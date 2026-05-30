class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result=0
        i=0
        j=len(heights)-1
        while i<j:
            smaller=min(heights[i],heights[j])
            water_stored=smaller*(j-i)
            result=max(water_stored,result)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return result