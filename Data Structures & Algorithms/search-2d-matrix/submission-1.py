class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            m=nums[-1]
            if target<=m:
                l,r=0,len(nums)-1
                while l<=r:
                    m=(l+r)//2
                    if nums[m]==target:
                        return True
                    if nums[m]<target:
                        l=m+1
                    else:
                        r=m-1
                return False
        return False
