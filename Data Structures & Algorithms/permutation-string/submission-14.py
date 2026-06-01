class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0 for i in range(26)]
        s2_count = [0 for i in range(26)]
        window_count = [0 for i in range(26)]
        l=0
        r = l + len(s1) - 1
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            s1_count[ord(s1[i])-97] +=1
            s2_count[ord(s2[i])-97] +=1
        
        while l<=r and r<len(s2):
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[l])-97] -=1
            l+=1
            r+=1
            if r<len(s2):
                s2_count[ord(s2[r])-97] +=1
            

        return False

            