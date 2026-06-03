class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for i in tokens:
            if i == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1+num2))
                continue
            if i == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1-num2))
                continue
            if i == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1*num2))
                continue
            if i == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1/num2))
                continue
            # print(i)
            stack.append(int(i))
            # print(stack)

        return int(stack.pop())
