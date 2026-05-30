class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        store1=[0]*26
        store2=[0]*26
        matched=0
        for i in range(len(s1)):
            store1[ord(s1[i])-ord('a')]+=1
            store2[ord(s2[i])-ord('a')]+=1
        for i in range(26):
            if store1[i] == store2[i]:
                matched+=1
        if matched==26:
            return True
        j=len(s1)
        i=0
        while i<j and j<len(s2):
            if matched==26:
                return True
            store2[ord(s2[j])-ord('a')]+=1
            if store2[ord(s2[j])-ord('a')] ==store1[ord(s2[j])-ord('a')]:
                matched+=1
            elif store2[ord(s2[j])-ord('a')] -1 == store1[ord(s2[j])-ord('a')]:
                matched-=1
            store2[ord(s2[i])-ord('a')]-=1
            if store2[ord(s2[i])-ord('a')] ==store1[ord(s2[i])-ord('a')]:
                matched+=1
            if store2[ord(s2[i])-ord('a')] + 1 ==store1[ord(s2[i])-ord('a')]:
                matched-=1
            i+=1
            j+=1
        return matched==26
            