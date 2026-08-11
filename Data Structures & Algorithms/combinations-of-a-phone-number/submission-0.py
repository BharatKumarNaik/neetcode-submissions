class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #                       34
        #                        3
        #        d               e                f
        # i+1   ghi             ghi              ghi
        # i+1>=len(digits) append to res
        if len(digits)==0:
            return []
        dataSet={"2":"abc","3":"def","4":"ghi","5":"jkl",
        "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        def backTracking(i,st):
            if i>=len(digits):
                res.append(st)
                return
            cur=digits[i]
            for val in dataSet[cur]:
                st+=val
                backTracking(i+1,st)
                st=st[:-1]
        
        backTracking(0,"")
        return res
