class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for i in range(len(strs)):
            itemp=''.join(sorted(strs[i]))
            if itemp not in result:
                result[itemp]=[strs[i]]
            else:
                continue
            for j in range(i+1,len(strs)):
                jtemp=''.join(sorted(strs[j]))
                print(itemp,jtemp)
                if itemp==jtemp:
                    result[itemp].append(strs[j])
        return result.values()