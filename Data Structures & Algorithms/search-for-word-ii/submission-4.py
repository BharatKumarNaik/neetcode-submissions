class Trie:
    def __init__(self):
        self.children={}
        self.EOW=False
    
    def addWord(self,word,i):
        arb=self
        for c in word:
            if c not in arb.children:
                arb.children[c]=Trie()
            arb=arb.children[c]
        arb.EOW=True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root=Trie()
        i=0
        for word in words:
            root.addWord(word,i)
            i+=1
        
        foundElements=set()
        def backtrack(r, c,arb=root,parsingWord=""):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or board[r][c]=="*"
            ):
                return
            char=board[r][c]
            if char not in arb.children:
                return

            parsingWord+=char
            board[r][c]="*"
            arb=arb.children[char]
            if arb.EOW:
                foundElements.add(parsingWord)

            backtrack(r + 1, c,arb, parsingWord)
            backtrack(r - 1, c,arb, parsingWord)
            backtrack(r, c + 1,arb, parsingWord)
            backtrack(r, c - 1,arb, parsingWord)
            board[r][c] = char
            return

        for i in range(ROWS):
            for j in range(COLS):
                backtrack(i,j)
        return list(foundElements)