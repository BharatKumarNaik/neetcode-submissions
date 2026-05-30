class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=len(s)-1
        j=0
        temp1=''
        temp2=''
        while i>=0 and j<len(s):
            if ord(s[i]) in range(97,123) or ord(s[i]) in range(65,91) or ord(s[i]) in range(48,58):
                temp1+=s[i].lower()
            if ord(s[j]) in range(97,123) or ord(s[j]) in range(65,91) or ord(s[j]) in range(48,58):
                temp2+=s[j].lower()
            i-=1
            j+=1
        return temp1==temp2