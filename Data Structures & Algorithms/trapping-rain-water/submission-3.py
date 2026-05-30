class Solution:
    def trap(self, height: List[int]) -> int:
        # 7 - (current_height - max(prev_mins) = 1) = 6
        # cur_min - prev_min * distance = 6
        # 12 - (current_height - max(prev_mins) = 2) =  10
        # still cur_min < = prev_min so jump to next point
        # 10 - (max(prev_mins) = 2) = 8
        # cur_min = 3 
        # 8 + 3 * (cur_min-prev_min=3-2 = 1) = 11
        # 11 - 1 -1 = 9
        l,r = 0, len(height)-1
        max_prev_min_heights = 0
        total_water = 0
        while l<r:
            min_height = min(height[l],height[r])
            prev_max = max_prev_min_heights
            max_prev_min_heights=max(max_prev_min_heights,min_height)
            distance = r - l
            total_water += distance * (max_prev_min_heights - prev_max)
            if height[l]<height[r]:
                l+=1
                total_water -= min(max_prev_min_heights,height[l])
            else:
                r-=1
                total_water -= min(max_prev_min_heights,height[r])
        return total_water
