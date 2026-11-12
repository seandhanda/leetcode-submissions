class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
#O(1) time
#O(1) space

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.root.isEnd = True
    #O(1) time
    #O(1) space

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
    #O(L) time
    #O(L) space
    
    def search(self, word: str) -> bool:
        curr = self.root
        
        def dfs(index: int, curr: Optional[TrieNode]) -> bool:
            for i in range(index, len(word),+1):
                if word[i] == ".":
                    for child in curr.children:
                        if dfs(i+1, curr.children[child]):
                            return True
                    return False
                if word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]
            if not curr.isEnd:
                return False
            return True

        return dfs(0, curr)

        #O(L * K^2) time
        #O(L) space
