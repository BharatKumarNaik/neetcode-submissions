class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,0
        tdata = {}
        result = s
        for i in t:
            tdata[i]=tdata.get(i,0)+1
        
        rflag = 0
        
        if len(t)>len(s):
            return ""
        while l<=r and r<len(s):
            if s[r] in tdata:
                tdata[s[r]]-=1
            while max(tdata.values())<=0:
                rflag = 1
                if len(result)>r-l+1:
                    result = s[l:r+1]
                if s[l] in tdata:
                    tdata[s[l]]+=1
                l+=1

            r+=1

        return result if rflag ==1 else ""