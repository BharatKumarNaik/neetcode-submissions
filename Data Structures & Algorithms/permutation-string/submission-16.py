class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0 for i in range(26)]
        s2_count = [0 for i in range(26)]
        l=0
        r = l + len(s1) - 1
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            s1_count[ord(s1[i])-97] +=1
            s2_count[ord(s2[i])-97] +=1
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches +=1
        # print(matches)
        # print(s2[l:r+1])
        # print(s1_count)
        # print(s2_count)
        while l<=r and r<len(s2):
            if matches == 26:
                return True
            if s2_count[ord(s2[l])-97] == s1_count[ord(s2[l])-97]:
                matches -=1
            s2_count[ord(s2[l])-97] -=1
            if s2_count[ord(s2[l])-97] == s1_count[ord(s2[l])-97]:
                matches +=1

            l+=1
            r+=1
            if r<len(s2):
                if s2_count[ord(s2[r])-97] == s1_count[ord(s2[r])-97]:
                    matches -=1
                s2_count[ord(s2[r])-97] +=1
                if s2_count[ord(s2[r])-97] == s1_count[ord(s2[r])-97]:
                    matches +=1
            # print(matches)
            # print(s2[l:r+1])
            # print(s1_count)
            # print(s2_count)
        return False

            