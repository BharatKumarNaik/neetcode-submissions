class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data={}
        for i in strs:
            val="".join(sorted(i))
            if val not in data:
                data[val]=[]
            data[val].append(i)
        return list(data.values())