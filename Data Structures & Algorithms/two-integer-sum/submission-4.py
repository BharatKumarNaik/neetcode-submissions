class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store={}
        for i in range(0,len(nums)):
            val=target-nums[i]
            if val in store:
                return [store[val],i]
            store[nums[i]]=i
        return [-1,-1]