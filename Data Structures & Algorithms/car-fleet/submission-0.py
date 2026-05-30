class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined=[(x,y) for x,y in zip(position,speed)]
        combined.sort(key=lambda x:x[0])
        stack=[]
        combined=combined[::-1]
        # print(combined)
        for i in combined:
            # print(stack)
            time=(target-i[0])/i[1]
            if len(stack)==0:
                stack.append(time)
                continue
            top=stack[-1]
            if top<time:
                stack.append(time)
        return len(stack)

