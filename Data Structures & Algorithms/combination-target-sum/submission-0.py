class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Combination means it's a backtracking problem
        # if it was two sum or 3 sum it wouldv'e been like recomputing target based on first digits
        # but in this case it can be of any combination
        # so we need to go dfs backtracking
        # with i or without i approach
        # along with it we also include i again
        # dfs(i+1) dfs(i) dfs(i+1)

        res=[]
        def dfs(i,subset,subTotal):
            if i>=len(nums) or subTotal>target:
                return
            elif subTotal==target:
                # print(i,subset)
                res.append(subset.copy())
                return

            subset.append(nums[i])
            subTotal+=nums[i]
            # with same i again
            dfs(i,subset,subTotal)
            # without i
            subset.pop()
            subTotal-=nums[i]
            dfs(i+1,subset,subTotal)

        dfs(0,[],0)
        return res