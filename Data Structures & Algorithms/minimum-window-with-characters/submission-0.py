class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # i and j as start and end
        # j+=1 untill we get all chrs
        # when we get it i+=1 and store it in result if j-i+1<len(result)
        # untill it ruins the t char counts
        # increment j+=1 untill we get all chrs
        s_data={}
        t_data={}
        result='None'*len(s)
        for i in t:
            if i not in t_data:
                t_data[i]=0
                s_data[i]=0
            t_data[i]+=1
        i=0
        for j in range(len(s)):
            if s[j] in s_data:
                s_data[s[j]]+=1
            flag=1
            for val in t_data:
                if t_data[val]>s_data[val]:
                    flag=0
            # print(s[i:j+1],flag)
            while flag:
                # print(s[i:j+1])
                if len(result)>j-i+1:
                    result=s[i:j+1]
                if s[i] in s_data:
                    s_data[s[i]]-=1
                    if s_data[s[i]]<t_data[s[i]]:
                        flag=0
                i+=1
        if len(result)>len(s):
            result=''
        return result
            