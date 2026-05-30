class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums) #to remove the duplicates
        result=0
        for i in numset:
            if i-1 not in numset: #It specifically identifies start of the sequence
                length=1 #considering current element as 1
                while i+length in numset: #checking every element comming after cuurent one
                    length+=1
                result=max(length,result)
        return result