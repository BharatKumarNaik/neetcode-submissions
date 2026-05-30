class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = sorted(nums)
        result = []
        if len(nums)<=3:
            if sum(nums)==0:
                result.append(nums)
                return result
            else:
                return []
        for i in range(len(numbers)-2):
            print(i)
            target = -1 * numbers[i]
            l,r = i+1, len(numbers)-1
            while l<r:
                cur_sum = numbers[l]+numbers[r]
                if cur_sum < target:
                    l+=1
                elif cur_sum> target:
                    r-=1
                else:
                    result.append(sorted([numbers[i],numbers[l],numbers[r]]))
                    l+=1
        print(result)
        final_result=[]
        for i in range(len(result)):
            if result[i] not in final_result:
                final_result.append(result[i])
        return final_result