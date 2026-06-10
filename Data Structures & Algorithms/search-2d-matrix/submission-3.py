class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j=0,len(matrix)-1
        while i<=j:
            rmid = (j+i)//2
            print(j,i,rmid)
            if target<matrix[rmid][0]:
                j=rmid-1
            elif target>matrix[rmid][-1]:
                i=rmid+1
            else:
                break
        i,j=0,len(matrix[rmid])-1
        # print(i,j)
        while i<=j:
            cmid = (j+i)//2
            # print(cmid)
            if target<matrix[rmid][cmid]:
                j = cmid - 1
            elif target>matrix[rmid][cmid]:
                i =cmid + 1
            else:
                return True
        return False