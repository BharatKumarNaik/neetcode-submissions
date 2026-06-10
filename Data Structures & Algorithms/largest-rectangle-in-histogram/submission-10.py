class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0
        heights.append(0)
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] -1
                else:
                    width = i
                result = max(result,height*width)
            stack.append(i)
        return result