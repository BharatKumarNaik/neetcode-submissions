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
        for word in words:
            root.addNode(word)
        
        res,visited=set(),set()
        def dfs(i,j,cur,parsed_word):
            if (i not in range(len(board)) or j not in range(len(board[0]))):
                return
            if((i,j) in visited or board[i][j] not in cur.children):
                return 

            visited.add((i,j))
            cur=cur.children[board[i][j]]
            parsed_word+=board[i][j]
            if cur.end==True:
                res.add(parsed_word)
            
            dfs(i+1,j,cur,parsed_word)
            dfs(i-1,j,cur,parsed_word)
            dfs(i,j+1,cur,parsed_word)
            dfs(i,j-1,cur,parsed_word)

            visited.remove((i,j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,root,'')
        return list(res)