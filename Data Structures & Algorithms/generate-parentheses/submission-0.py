class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        result=[]
        def recursion(opn,cls):
            if opn==cls==n:
                result.append(''.join(stack))
                return
            if opn<n:
                stack.append('(')
                recursion(opn+1,cls)
                stack.pop()
            if cls<opn:
                stack.append(')')
                recursion(opn,cls+1)
                stack.pop()
        recursion(0,0)
        return result