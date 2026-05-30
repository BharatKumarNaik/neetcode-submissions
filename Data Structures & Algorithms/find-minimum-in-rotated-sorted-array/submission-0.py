class Solution:
    def findMin(self, nums: List[int]) -> int:
        def min_search(l,r):
            if l>r:
                return 1000
            if l==r:
                return nums[l]
            mid=(l+r)//2
            return min(nums[mid],min_search(mid+1,r),min_search(l,mid-1))
        return min_search(0,len(nums)-1)