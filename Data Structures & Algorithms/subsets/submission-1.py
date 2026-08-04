class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            #                           []
            #                   /with 1      \without 1
            #                [1]                    []
            #             /      \               /      \
            #         [1,2]      [1]         [2]        []
            #        /    \      /  \       /   \      /   \
            #  [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3]  []   
            res=[]
            def dfs(i,subset):
                if i>=len(nums):
                    # we reached leaf node
                    # time to store it in the res
                    res.append(subset.copy())
                    return
                # with i
                subset.append(nums[i])
                dfs(i+1,subset)
                # without i
                subset.pop()
                dfs(i+1,subset)
            
            dfs(0,[])
            return res
