class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            if ord(s[i]) in range(97,123) or ord(s[i]) in range(65,91) or ord(s[i]) in range(48,58):
                val1=s[i].lower()
            else:
                i+=1
                continue
            if ord(s[j]) in range(97,123) or ord(s[j]) in range(65,91) or ord(s[j]) in range(48,58):
                val2=s[j].lower()
            else:
                j-=1
                continue
            if val1!=val2:
                return False
            i+=1
            j-=1
        return True