class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n=2
        #                          ( #1,0
        #               ) #1,1                            ( #2,0
        #               (  #i==j                 )#2,1               )
        #   	  (              )          )           (               )
        self.res=[]
        def backTracking(st,o,c):
            if o==c and c==n:
                self.res.append(st)
                return 
            if o<n:
                st+="("
                backTracking(st,o+1,c)
                st=st[:-1]
            if c<o:
                st+=")"
                backTracking(st,o,c+1)
                st=st[:-1]
            return
        backTracking("",0,0)
        return self.res
