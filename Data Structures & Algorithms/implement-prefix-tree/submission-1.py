class Tree:
    def __init__(self,):
        self.children={} #Dict
        self.endOfWord=False # This is to indicate if there is any word which ends at this point or not

class PrefixTree:

    def __init__(self):
        self.root=Tree()

    def insert(self, word: str) -> None:
        arb=self.root
        for char in word:
            if char not in arb.children:
                arb.children[char]=Tree()
            arb=arb.children[char]
        # added or reached the end of the word
        arb.endOfWord=True

    def search(self, word: str) -> bool:
        arb = self.root
        for char in word:
            if char in arb.children:
                arb=arb.children[char]
                continue
            return False
        if arb.endOfWord: #check if that is actually a word or not
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        arb=self.root
        for char in prefix:
            if char in arb.children:
                arb=arb.children[char]
                continue
            return False
        # I don't have to check if the word is ending or not as it's a prefix
        return True