class SegmentTree:
    def __init__(self,N,nums):
        self.n = 1
        while self.n<N:
            self.n *= 2
        self.build(N,nums)

    def build(self,N,nums):
        self.tree = [float('-inf')] * self.n * 2
        # Don't do [float('-inf')] * self.n + N
        # because if N is odd it's, for it's root node calculation we will not have two nodes.
        
        # assign list values to the leaf nodes
        for i in range(N):
            self.tree[self.n+i] = nums[i]

        # start creating the upper nodes/root nodes
        for i in range(self.n-1,0,-1):
            # traversing in reverse order as root node calculation is dependent on it's respective leaf node
            self.tree[i] = max(self.tree[i<<1],self.tree[i<<1|1])
            # i >> 1 | 1 is performing 2*i+1 operation
            # To fetch it's respective child node.
        
    def query(self,l,r):
        l+=self.n
        r+=self.n
        res = float('-inf')
        while l<=r:
            if l&1:
                # l is Odd
                # Indicates l is in the range but l's parent node will be outof scope of l:r range
                # so we store the l in res and move the l to next segment as l+1 's parent will be in the l:r range
                # It must be visualized in the graph format for better understanding.
                res = max(res,self.tree[l])
                l+=1
            if r&1 ==0:
                # r is even
                # Indicates r's parent node is is outofscope segment but r is in required range
                # so we store the result and move it backward so that it's parent is in the l:r range
                res = max(res,self.tree[r])
                r-=1
            l>>=1
            r>>=1
            # move to there respective parent nodes
        return res
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Tree = SegmentTree(len(nums),nums)
        result = []
        l = 0
        r = l+k-1
        while l<=r and r<len(nums):
            result.append(Tree.query(l,r))
            l+=1
            r+=1
        return result
