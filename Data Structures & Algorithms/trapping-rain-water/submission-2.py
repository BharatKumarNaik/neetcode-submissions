class Solution:
    def trap(self, height: List[int]) -> int:
        result=0
        i=0
        j=len(height)-1
        prev_min_max=0
        while i<j:
            min_height=min(height[i],height[j])
            if min_height<prev_min_max:
                result-=min_height
            elif min_height!=0:
                stored_assumption=(min_height-prev_min_max)*(j-i-1)
                result+=stored_assumption
                result-=min(prev_min_max,min_height)
                prev_min_max=max(prev_min_max,min_height)
            # print(f'{[i,j]},{[height[i],height[j]]} = {result}')
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return result
            