class Solution:
    def trap(self, height: List[int]) -> int:
        # min(i,j)
        # if cmin>mmin:
        # += cmin-mmin *(j-i)
        # 
        # -=min(cmin,mmin)
        # mmin=max(mmin,cmin)

        i,j=0,len(height)-1
        mmin=0
        result=0
        while i<j:
            cmin=min(height[i],height[j])
            if cmin>mmin:
                result+=(cmin-mmin) * (j-i-1)
            print(result)
            result-=min(cmin,mmin)
            mmin=max(mmin,cmin)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return result