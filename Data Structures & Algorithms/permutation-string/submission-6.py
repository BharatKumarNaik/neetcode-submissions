class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        n=len(s1)
        while i<=len(s2)-n:
            # print(i,i+n-1)
            j=i
            data={}
            for val in s1:
                if val not in data:
                    data[val]=0
                data[val]+=1
            while j<i+n:
                # print(f'{data} inside')
                if s2[j] in data and data[s2[j]]>0:
                    data[s2[j]]-=1
                else:
                    break
                j+=1
            # print(data)
            if sum(data.values())==0:
                return True
            i+=1
        return False