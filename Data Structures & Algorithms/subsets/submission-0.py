class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i,subset):
            if i>=len(nums):
                res.append(subset.copy())
                return
            # include i and send it to next
            subset.append(nums[i])
            dfs(i+1,subset)
            # exclude i and and send it to next step
            subset.pop()
            dfs(i+1,subset)
        dfs(0,subset)
        return res