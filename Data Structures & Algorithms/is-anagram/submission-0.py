class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_data={}
        for i in s:
            if i not in s_data:
                s_data[i]=0
            s_data[i]+=1
        for j in t:
            if j in s_data and s_data[j]>0:
                s_data[j]-=1
            else:
                return False
        if sum(s_data.values())!=0:
            return False
        return True