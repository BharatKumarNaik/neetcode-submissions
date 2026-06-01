class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i]>=height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    left = height[stack[-1]]
                    right = height[i]
                    ws_height = min(left,right) - mid
                    distance =  i - stack[-1] - 1
                    result += ws_height * distance
            stack.append(i)
        return result