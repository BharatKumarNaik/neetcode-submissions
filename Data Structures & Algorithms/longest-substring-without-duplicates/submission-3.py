class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=i+1
        result=1
        if len(s)==1:
            return 1
        elif len(s)==0:
            return 0
        while i<len(s)-1 and j<len(s):
            if s[j] not in s[i:j]:
                result=max(result,j-i+1)
                j+=1
            else:
                i+=1
        return result