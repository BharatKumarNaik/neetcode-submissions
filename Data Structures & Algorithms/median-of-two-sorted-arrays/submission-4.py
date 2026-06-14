class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find the min list and consider it as nums1
        # [4,6,7] 
        # [1,2,3,4,5,6]
        n = len(nums1)
        m = len(nums2)
        if n>m:
            n,m=m,n
            nums1,nums2=nums2,nums1
        mid = (n+m)//2
        # find the mid of the smaller list which is nums1
        # set the window from l - m1 and consider rest of the size in nums2 list
        # which is m1 - l + 1 - mid, so index of m2 = (m1 - l + 1) - (mid - 1)
        # check the condition
        # if nums1[m1]<nums2[m2+1] and if nums2[m2]<nums1[m1+1]: True -> left portion is ready
        # if nums1[m1]>nums2[m2+1] move the r1 to m1 such that new m1 moves towards left
        # and causes the list to avoid higher elements.
        # recompute the m2 based on new m1
        l,r = 0, len(nums1)-1
        while True:
            i = (l+r)//2 # nums1 leftportion
            j = mid - i - 2 # nums2 left portion
            Aleft = nums1[i] if i>=0 else float("-infinity")
            Aright = nums1[i+1] if (i+1)<n else float("infinity")

            Bleft = nums2[j] if j>=0 else float('-infinity')
            Bright = nums2[j+1] if j+1<m else float('infinity')

            if Aleft<=Bright and Bleft<=Aright:
                if (n+m)%2==0:
                    # Even
                    return (max(Aleft,Bleft) + min(Aright,Bright))/2
                else:
                    # Odd
                    return min(Aright,Bright)
            elif Aleft>Bright:
                r = i - 1
            else:
                l = i + 1
