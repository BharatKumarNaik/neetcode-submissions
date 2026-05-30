class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        max_storage = 0
        while l<r:
            min_height = min(heights[l],heights[r])
            water_store = min_height * (r-l)
            # print(min_height,l,r)
            max_storage = max(max_storage,water_store)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_storage