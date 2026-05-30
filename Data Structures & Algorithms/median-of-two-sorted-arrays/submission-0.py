class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=[]
        i,j=0,0
        n=len(nums1)
        m=len(nums2)
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i<n:
            res.append(nums1[i])
            i+=1
        while j<m:
            res.append(nums2[j])
            j+=1
        r=n+m
        print(res)
        if r%2==0:
            mid1=r//2
            mid2=(r//2)-1
            return (res[mid1]+res[mid2])/2
        else:
            mid1=r//2
            return res[mid1]
        

            