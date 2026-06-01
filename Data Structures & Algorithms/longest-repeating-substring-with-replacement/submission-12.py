class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        data = {}
        l,r = 0,0
        result = 0
        while l<=r and r<len(s):
            if s[r] not in data:
                data[s[r]] = 0
            data[s[r]]+=1

            if sum(data.values()) - max(data.values()) <= k:
                result = max(result,r-l+1)
            else:
                data[s[l]] -=1
                l += 1
            r+=1
            print(data,l,r)
        return result
