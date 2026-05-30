class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = sorted(nums)
        if len(nums)<=3:
            if sum(nums)==0:
                return [nums]
            else:
                []
        result = {}
        for i in range(len(nums)-2):
            target = -1 * numbers[i]
            l,r = i+1, len(nums)-1
            while l<r:
                cur_sum = numbers[l]+numbers[r]
                if cur_sum < target:
                    l+=1
                elif cur_sum > target:
                    r-=1
                else:
                    # means they are equal
                    key = f"{numbers[i]},{numbers[l]},{numbers[r]}"
                    if key not in result:
                        result[key]=[numbers[i],numbers[l],numbers[r]]
                    l+=1
        print(result.values())
        return list(result.values())