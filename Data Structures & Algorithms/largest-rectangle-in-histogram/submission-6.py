class SegmentTree:
    def __init__(self,N,A):
        self.n = 1
        self.N = N
        while self.n<=N:
            self.n*=2
        self.A = A.copy()
        i = N
        while i < (self.n):
            self.A.append(float('inf'))
            i+=1
        self.build()

    def min_index_cal(self,i,j):
        if self.A[i]<self.A[j]:
            return i
        else:
            return j

    def build(self):
        self.tree = [float('inf')] * (self.n*2)
        # Tree Leaf Node: will contain the index of actual data
        for i in range(self.n):
            self.tree[self.n+i] = i
        for i in range(self.n-1,0,-1):
            # for a given node: need to check right and left child
            left_child = i<<1
            right_child = i<<1 | 1
            # print(self.tree)
            # print(left_child,right_child)
            if self.tree[right_child]<self.n and left_child>0 and self.A[self.tree[right_child]]<self.A[self.tree[left_child]]:
                self.tree[i] = self.tree[right_child]
            else:
                self.tree[i] = self.tree[left_child]
        # print(self.tree)

    def query(self,l,r):
        min_index = l
        l+=self.n
        r+=self.n
        # print("query")
        while l<=r:
            if l&1:
                # print("odd l",self.tree[l])
                min_index = self.min_index_cal(min_index,self.tree[l])
                l+=1
            if r&1==0:
                # Even
                # print("even r",self.tree[r])
                min_index = self.min_index_cal(min_index,self.tree[r])
                r-=1
            l>>=1
            r>>=1
        return min_index
        

         
class Solution:
    def maxArea(self, l, r, A,STree):
        # print(A)
        if l>=len(A) or r>=len(A):
            return 0
        if l<0 or r<0:
            return 0
        if l>r:
            return 0
        if l==r:
            if l<len(A):
                return A[l]
            else:
                return 0
        min_index = STree.query(l,r)
        # print(l,r,min_index)
        return max(max(self.maxArea(l,min_index-1,A,STree),self.maxArea(min_index+1,r,A,STree)),(r-l+1)*A[min_index])

    def largestRectangleArea(self, heights:List[int]) -> int:
        # Segment Tree Method
        # Segment tree to get the min_index of the heights given the range
        # recursive function call to get the area between l and r with min_height
        # then checking left and right side of the min_index to calculate the area.
        stack = []
        max_area = 0

        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area