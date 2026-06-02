class SegmentTree:
    def __init__(self,N,nums):
        self.n = 1
        while self.n<N:
            self.n = self.n * 2
        self.build(N,nums)
    
    def build(self,N,nums):
        self.tree = [float('-inf')] * self.n * 2
        for i in range(N):
            self.tree[i+self.n] = nums[i]
        
        for i in range(self.n-1,0,-1):
            self.tree[i]= max(self.tree[i<<1], self.tree[i << 1 | 1])
            # i << 1 | 1 is just (2*i)+1
    
    def query(self,l,r):
        res = float('-inf')
        l+=self.n
        r+=self.n
        while l<=r:
            if l & 1:
                # l is Odd
                res = max(res,self.tree[l])
                l+=1
            if r & 1 ==0:
                # r is Even
                res = max(res,self.tree[r])
                r-=1
            l>>=1
            r>>=1
        return res
        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Tree = SegmentTree(len(nums),nums)
        result=[]
        l = 0
        r = l+k-1
        while l<=r and r<len(nums):
            result.append(Tree.query(l,r))
            l+=1
            r+=1
        return result