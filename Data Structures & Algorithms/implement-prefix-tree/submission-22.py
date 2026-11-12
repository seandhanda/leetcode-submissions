class TrieNode:
    def __init__(self):
        self.children = {} 
        self.isEnd = False
    #O(1) time
    #O(1) space

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        self.root.isEnd = True
    #O(1) time
    #O(1) space

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
        curr.isEnd = True
    #O(L) time
    #O(L) space

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        if not curr.isEnd:
            return False
        return True
        #O(L) itme
        #O(1) space 


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        return True
        #O(L) time
        #O(1) space
        