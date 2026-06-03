class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        leftmax = [float('-inf')]* n
        rightmax = [float('-inf')]*n

        for i in range(n):
            # leftmax
            if i % k == 0:
                leftmax[i] = nums[i]
            else:
                leftmax[i] = max(leftmax[i-1], nums[i])

            # rightmax
            j = n - 1 - i

            if j == n - 1 or j % k == 0:
                # In case of leftmax first element will definitly will be start of block
                # but in case of rightmax, as we are moving in reverse order, last element may not be start of the block.
                # That's why we include the condition even if j%k is !=0 still make the last element as start of the block.
                rightmax[j] = nums[j]
            else:
                rightmax[j] = max(rightmax[j+1], nums[j])
        
        output =[]
        # print(leftmax)
        # print(rightmax)
        for i in range(n-k+1):
            output.append(max(leftmax[i+k-1],rightmax[i]))
        return output
