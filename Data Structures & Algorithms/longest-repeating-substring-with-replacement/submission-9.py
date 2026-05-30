class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s[i] -> counter{}  +1
        # if len(substring)-max(countervalues)<k means valid
        # if condition is invalid i+=1 untill condition is valid
        # need to ensure counter -1
        # if valid then need to update res
        result=0
        i,j=0,0
        data={}
        while j<len(s):
            if s[j] not in data:
                data[s[j]]=0
            data[s[j]]+=1
            while (j-i+1)-max(data.values())>k:
                data[s[i]]-=1
                i+=1
            result=max(result,j-i+1)
            j+=1
        return result


