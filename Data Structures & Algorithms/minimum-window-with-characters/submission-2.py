class Solution:
    def minWindow(self, s: str, t: str) -> str:
        store1=[0]*58
        store2=[0]*58
        for i in t:
            index=ord(i)-ord('A')
            store1[index]+=1

        matched=0
        for i in range(58):
            if store2[i] >= store1[i]:
                matched+=1
        i,j=0,0
        result_n=1001
        result=''
        while i<=j and j<len(s):
            index=ord(s[j])-ord('A')
            store2[index]+=1
            if store2[index]-1 >= store1[index] and store2[index] < store1[index]:
                #Before it was greater/equal now it become less
                matched -=1
            if store2[index]-1 < store1[index] and store2[index]>=store1[index]:
                #before it was less and now it become greater or equal
                matched +=1
            # if both before and after is greater or equal remains same
            while matched==58 and i<=j:
                # print(s[i:j+1])
                temp=j-i+1
                if temp<result_n:
                    result_n=temp
                    result=s[i:j+1]
                index=ord(s[i])-ord('A')
                store2[index]-=1
                if store2[index]<store1[index] and store2[index] + 1 >=store1[index]:
                    #before it was greater/equal now become less
                    matched-=1
                elif store2[index]>=store1[index] and store2[index]+1<store1[index]:
                    # before it was less and now it become grater or equal which will not happen here
                    matched +=1
                i+=1
            j+=1
        return result