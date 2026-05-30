class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker={}
        i=0
        j=0
        result=0
        while i<len(s) and j<len(s):
            if s[j] in tracker:
                i=max(tracker[s[j]]+1,i)
            tracker[s[j]]=j
            # print(s[i:j+1],[i,j])
            result=max(result,j-i+1)
            j+=1
        return result