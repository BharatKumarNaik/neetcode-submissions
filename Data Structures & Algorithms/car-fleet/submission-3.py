class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [4,1,0,6,-1]
        # [3,5,10,4,4]        
        # # adjsted step
        # [4,5,10,4,5]
        # data = [(4,2),(1,2),(0,1),(7,1),(-1,3)]
        data = [x for x in zip(position,speed)]
        data=sorted(data,key=lambda x:x[0],reverse = True)
        steps = []
        i=0
        for i in range(len(position)):
            # print(data[i])
            step = (target-data[i][0])/data[i][1]
            # print(step)
            if steps and step<steps[-1]:
                step = steps[-1]
            steps.append(step)
            # print(steps)
        # return the distinct count of the steps list
        return len(set(steps))
            
        





