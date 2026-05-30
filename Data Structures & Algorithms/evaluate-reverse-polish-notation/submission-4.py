class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            # print(stack)
            if i not in ['+','-','/','*']:
                stack.append(i)
                continue
            a=int(stack.pop())
            b=int(stack.pop())
            match i:
                case '+':
                    c=b+a
                case '-':
                    c=b-a
                case '/':
                    c=b/a
                case '*':
                    c=b*a
            stack.append(c)
        return int(stack.pop())