class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            if len(stack)==0:
                return False
            match i:
                case ')':
                    if stack.pop()!='(':
                        return False
                case '}':
                    if stack.pop()!='{':
                        return False
                case ']':
                    if stack.pop()!='[':
                        return False
        return len(stack)==0        