class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Bruteforce
        # chose one after another
        #        1           2              3
        #    2       3   1       3       1      2
        #    3       2   3       1       2      1
        if nums and len(nums)==0:
            return [[]]
        res=[]
        for i in nums:
            cpy=nums.copy()
            cpy.remove(i)
            # print(cpy,i)
            permutation=self.permute(cpy)
            if len(permutation)==0:
                return [[i]]
            for p in permutation:
                cur=[i]+p
                res.append(cur)
        return res