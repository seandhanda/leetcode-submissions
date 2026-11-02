class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}
    #O(1) time
    #O(1) space

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    #O(1) time
    #O(1) space

    def addWord(self, word: str) -> None:
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
        
        def dfs(index: int, curr: TrieNode) -> bool:
            for i in range(index, len(word),+1):
                if word[i] == ".":
                    for child in curr.children:
                        if dfs(i+1, curr.children[child]):
                            return True
                    return False
                if word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]
            if curr.isEnd == False:
                return False
            return True


        return dfs(0,curr)

    #O(L * k^2) time
    #O(L) space
