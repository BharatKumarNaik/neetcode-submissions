class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # [1,2,3,4,5]
        # [3,5,6,8]
        # first take the bigger list as the base list for easier windowing
        n,m = len(nums1),len(nums2)
        if n<m:
            n,m=m,n
            nums1,nums2 = nums2,nums1
        # main moto will be to form the left section of middle element
        mid = (n+m)//2
        nj = mid - 1
        mj = -1
        # In the loop we need to check 
        # if the nums1[nj]<nums2[mj+1] and if mj and nums2[mj]<nums1[nj+1]
        # till then we need decrease the nj and increment the mj one after other
        # Need to run the loop till it fails
        while (mj+1<m and nums1[nj]>nums2[mj+1]) or (mj>=0 and mj<m and nj+1<n and nums2[mj]>nums1[nj+1]):
            nj-=1
            mj+=1
            # print(nj,mj)
        # print(nums[ni:nj])
        # print(nums[mi:mj])
        # check if n + m is odd or even
        if (n+m)%2==0:
            # Even
            # left partition's max
            if mj>=0 and nj>=0:
                first_ele = max(nums1[nj],nums2[mj])
            elif mj>=0:
                first_ele = nums2[mj]
            elif nj>=0:
                first_ele = nums1[nj]
            # Need to find the right portion's min
            if mj+1<m and nj+1<n:
                second_ele = min(nums1[nj+1],nums2[mj+1])
            elif mj+1<m:
                second_ele = nums2[mj+1]
            elif nj+1<n:
                second_ele = nums1[nj+1]
            return (first_ele+second_ele)/2
        else:
            # Odd
            if nj+1>=n:
                return float(nums2[mj+1])
            elif mj+1>=m:
                return float(nums1[nj+1])
            else:
                # both are in bound
                return float(min(nums1[nj+1],nums2[mj+1]))

        

