class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # optimal stack approach
        stack = []
        heights.append(0)
        maxArea = 0
        # making sure end of the heights array has one min height which will be 0
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i-stack[-1] - 1
                maxArea = max(maxArea, height*width)
            stack.append(i)
        return maxArea