class TrieNode:
    def __init__(self):
        self.childrens={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.node=TrieNode()

    def addWord(self, word: str) -> None:
        i=0
        arb=self.node
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
        # .ab  ab. abc  abc.ab
        def rec_search(word,node):
            i=0
            arb=node
            while i<len(word):
                if word[i]=='.':
                    for k in arb.childrens:
                        if rec_search(word[i+1:],arb.childrens[k]):
                            return True
                    return False
                if word[i] in arb.childrens:
                    arb=arb.childrens[word[i]]
                else:
                    return False
                i+=1
            if arb.end==True:
                return True
            else:
                return False
        return rec_search(word,self.node)
