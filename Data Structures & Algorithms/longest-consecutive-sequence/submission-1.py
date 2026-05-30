class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums) #to remove the duplicates
        result=0
        for i in numset:
            length=0
            while i+length in numset:
                length+=1
            result=max(length,result)
        return result