class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,subset,subTotal):
            if subTotal==target:
                # print(subset)
                res.append(subset.copy())
                return

            if i>=len(candidates) or subTotal>target:
                return
            
            # with i
            subset.append(candidates[i])
            subTotal+=candidates[i]
            dfs(i+1,subset,subTotal)

            # without i
            subset.pop()
            subTotal-=candidates[i]
            # ṣince we have dupliate values, we need to ignore those as well
            # to achieve this we've sorted the candidates
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,subset,subTotal)

        dfs(0,[],0)
        return res