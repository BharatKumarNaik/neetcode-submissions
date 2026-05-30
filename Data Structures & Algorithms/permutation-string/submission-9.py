class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(26+n) = O(n)
        # creating empty dict with a-z char
        if len(s1)>len(s2):
            return False
        data1={}
        data2={}
        for i in range(ord('a'),ord('z')+1):
            data1[chr(i)]=0
            data2[chr(i)]=0
        
        # filling first window charecter count in data1 and data2
        # based on s1 and s2 respectively
        i=0
        while i<len(s1):
            data1[s1[i]]+=1
            data2[s2[i]]+=1
            i+=1
        
        # matches check
        matches=0
        for i in data1:
            if data1[i]==data2[i]:
                matches+=1
        i=0
        for j in range(len(s1),len(s2)):
            if matches==26:
                return True
            data2[s2[j]]+=1
            if data2[s2[j]]==data1[s2[j]]:
                matches+=1
            elif data2[s2[j]]==data1[s2[j]]+1:
                matches -=1
            
            data2[s2[i]]-=1
            if data2[s2[i]]==data1[s2[i]]:
                matches+=1
            elif data2[s2[i]]==data1[s2[i]]-1:
                matches-=1
            i+=1
        return matches==26