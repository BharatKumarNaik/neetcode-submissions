class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        data = {}
        result = 0
        for r in range(len(s)):
            if s[r] in data:
                l = max(l,data[s[r]]+1)
            data[s[r]] = r
            result = max(result, r-l+1)
        return result
