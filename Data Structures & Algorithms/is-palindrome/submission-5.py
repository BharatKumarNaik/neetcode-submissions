class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        temp=list(map(lambda x: x if ord(x) in range(97,123) or ord(x) in range(48,58) else "","".join(s.split(' '))))
        s="".join(temp)
        i=0
        j=len(s)-1
        while i<=j:
            if s[i]==s[j]:
                i+=1
                j-=1
                continue
            return False
        return True