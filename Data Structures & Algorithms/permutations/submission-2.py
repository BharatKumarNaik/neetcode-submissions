class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # chose one after another
        #        1           2              3
        #    2       3   1       3       1      2
        #    3       2   3       1       2      1
        # Refer to the oldest commit of the day for easy solution
        # optimzation compared to previous solution:
        # time complexity wise both are O(n. n!)
        # but .copy() and .remove(i) puts more load on CPU cache
        # so, in this code our air will be to avoid it

        res=[]
        # picked list will store the boolean value 
        # which indicates which values are already used.
        def backtracking(nums,picked):
            if len(nums)==0:
                return []
            
            cur=[]
            for i in range(len(nums)):
                if picked[i]==False:
                    picked[i]=True
                    permutations=backtracking(nums,picked)
                    picked[i]=False
                    if len(permutations)==0:
                        return [[nums[i]]]
                    for p in permutations:
                        p.append(nums[i])
                        cur.append(p)
            return cur
        
        res=backtracking(nums,[False]*len(nums))
        return res