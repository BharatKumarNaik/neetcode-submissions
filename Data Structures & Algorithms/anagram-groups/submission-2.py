class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data={}
        for i in strs:
            chrlist=[0]*26
            for j in i:
                chrlist[ord(j)-ord('a')]+=1
            chrlist=str(chrlist)
            if chrlist not in data:
                data[chrlist]=[]
            data[chrlist].append(i)
        return list(data.values())