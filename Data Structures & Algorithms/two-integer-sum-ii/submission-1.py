class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            temp=target-numbers[i]-numbers[j]
            if temp==0:
                return [i+1,j+1]
            if temp<0:
                j-=1
            else:
                i+=1
        return [-1,-1]

