class Tree:
    def __init__(self,):
        self.children={}
        self.EOW=False

class WordDictionary:

    def __init__(self):
        self.root=Tree()

    def addWord(self, word: str) -> None:
        arb = self.root
        for char in word:
            if char not in arb.children:
                arb.children[char]=Tree()
            arb=arb.children[char]
        arb.EOW=True

    def search(self, word: str, start=None) -> bool:
        if start == None:
            arb=self.root
        else:
            arb=start
        for i in range(len(word)):
            if word[i]==".":
                for child in arb.children:
                    temp=self.search(word[i+1:],arb.children[child])
                    if temp:
                        return temp
                return False # No val is there to ignore
            if word[i] in arb.children:
                arb=arb.children[word[i]]
                continue
            return False
        return arb.EOW
