class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        data1={}
        data2={}
        for i in range(97,123):
            data1[chr(i)]=0
            data2[chr(i)]=0
        for i in s1:
            data1[i]+=1
        i=0
        j=0
        k=len(s1)
        while j<len(s2):
            data2[s2[j]]+=1
    
            if j-i+1==k:
                # print('inside')
                # print(data1,data2)
                if data1==data2:
                    return True
                data2[s2[i]]-=1
                i+=1
            j+=1
        return False
            