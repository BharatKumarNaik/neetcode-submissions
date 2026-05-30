class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data_dict ={}
        for s in strs:
            count=[0]*26
            for i in s:
                count[ord('a')- ord(i)]+=1
            if str(count) not in data_dict:
                data_dict[str(count)]=[]
            data_dict[str(count)].append(s)
        return list(data_dict.values())
