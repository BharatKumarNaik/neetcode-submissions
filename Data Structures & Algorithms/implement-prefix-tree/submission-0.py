class TrieNode:
    def __init__(self):
        self.childrens={}
        self.end=False
class PrefixTree:

    def __init__(self):
        self.node=TrieNode()

    def insert(self, word: str) -> None:
        arb=self.node
        i=0
        while i<len(word):
            if word[i] in arb.childrens:
                arb=arb.childrens[word[i]]
            else:
                break
            i+=1
        while i<len(word):
            arb.childrens[word[i]]=TrieNode()
            arb=arb.childrens[word[i]]
            i+=1
        arb.end=True

        return

    def search(self, word: str) -> bool:
        arb=self.node
        i=0
        while i<len(word):
            if word[i] in arb.childrens:
                arb=arb.childrens[word[i]]  
            else:
                return False
            i+=1      
        if arb.end==True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        arb=self.node
        i=0
        while i<len(prefix):
            if prefix[i] in arb.childrens:
                arb=arb.childrens[prefix[i]]
            else:
                return False
            i+=1
        return True

# {"a":[],"c":[]}