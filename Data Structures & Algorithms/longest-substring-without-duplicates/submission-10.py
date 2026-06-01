class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,1
        if len(s) ==0:
            return 0
        result = 1
        index_dict = {s[l]:0}
        while r<len(s) and l<r:
            while r<len(s) and s[r] not in s[l:r]:
                index_dict[s[r]]=r
                r+=1
            result = max(result,r-l)
            if r<len(s):
                l = index_dict[s[r]] + 1
                index_dict[s[r]] = r
                r+=1
        return result
            