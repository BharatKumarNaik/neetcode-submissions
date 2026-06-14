class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n>m:
            A = nums2
            B = nums1
            n,m = m,n
        else:
            A = nums1
            B = nums2
        
        MID = (n+m)//2
        l,r = 0, n-1
        while True:
            m1 = (l+r)//2
            m2 = (MID - 1) - (m1+1)
            Aleft = A[m1] if m1>=0 else float('-infinity')
            Aright = A[m1+1] if m1+1<n else float('infinity')
            Bleft = B[m2] if m2>=0 else float('-infinity')
            Bright = B[m2+1] if m2+1<m else float('infinity')
            if Aleft<=Bright and Bleft<=Aright:
                if (n+m)%2==0:
                    # even
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
                else:
                    # odd
                    return float(min(Aright,Bright))
            elif Aleft>Bright:
                r = m1 - 1
            else:
                l = m1 + 1