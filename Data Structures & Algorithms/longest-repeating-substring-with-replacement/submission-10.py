class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0
        win_dict={}
        result=0
        while i<=j and j<len(s):
            if s[j] not in win_dict:
                win_dict[s[j]]=0
            win_dict[s[j]]+=1
            max_val=max(list(win_dict.values()))
            print(s[i:j+1])
            while (j-i+1)-max_val>k and i<j:
                win_dict[s[i]]-=1
                i+=1
            print(s[i:j+1])
            result=max(result,j-i+1)
            j+=1
        return result
