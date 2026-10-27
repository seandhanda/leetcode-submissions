class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        self.root.isEnd = True

    #O(1) time
    #O(1) space

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return

        curr = self.root

        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
        curr.isEnd = True
        return

    #O(L) time
    #O(L) space

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True

        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False
            else:
                curr = curr.children[word[i]]
        if curr.isEnd:
            return True
        else:
            return False
        
        #O(L) time
        #O(1) space

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True

        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.children:
                return False
            else:
                curr = curr.children[prefix[i]]
        return True

        #O(L) time
        #O(1) space
        