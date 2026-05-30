class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        data={}
        i,j=0,0
        result=0
        while j<len(s):
            # print(i,j)
            if s[j] not in data:
                data[s[j]]=0
            data[s[j]]+=1
            while j-i+1-max(data.values())>k:
                data[s[i]]-=1
                i+=1
            # print(data)
            result=max(result,j-i+1)
            j+=1
        return result


