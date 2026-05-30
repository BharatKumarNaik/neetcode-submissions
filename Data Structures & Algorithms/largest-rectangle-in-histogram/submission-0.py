class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force
        result=0
        i=0
        while i<len(heights):
            result=max(result,heights[i])
            t_min=heights[i]
            j=i-1
            while j>=0:
                t_min=min(t_min,heights[j]) 
                # print(j,i)
                # print(f'result => {t_min},{t_min*(i-j+1)}')
                result=max(result,t_min*(i-j+1))
                j-=1
            i+=1
        return result