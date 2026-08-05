class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
            #                           []
            #                   /with 1      \without 1
            #                [1]                    []
            #             /      \               /      \
            #         [1,2]      [1]         [2]        []
            #        /    \      /  \       /   \      /   \
            #  [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3]  []  
        nums.sort()
        self.res=[]
        def dfs(i,subset):
            if i>=len(nums):
                # print(subset)
                self.res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            while i+1<len(nums) and nums[i+1]==nums[i]:
                i+=1
            dfs(i+1,subset)

        
        dfs(0,[])
        return self.res