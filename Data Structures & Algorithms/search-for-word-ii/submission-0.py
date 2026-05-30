class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
    def addNode(self,word):
        cur=self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch]=TrieNode()
            cur=cur.children[ch]
        cur.end=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        rows,cols=len(board),len(board[0])
        n=len(words)
        for word in words:
            root.addNode(word)

        res,visited=set(),set()
        def dfs(i,j,k,node,word):
            if i<0 or j<0 or i>=rows or j>=cols:
                return False
            if (i,j) in visited or board[i][j] not in node.children:
                return False
            node=node.children[board[i][j]]
            word+=board[i][j]
            visited.add((i,j))
            if node.end==True:
                res.add(word)
            dfs(i+1,j,k+1,node,word)
            dfs(i-1,j,k+1,node,word)
            dfs(i,j+1,k+1,node,word)
            dfs(i,j-1,k+1,node,word)
            visited.remove((i,j))
            return
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,0,root,'')
        return list(res)
