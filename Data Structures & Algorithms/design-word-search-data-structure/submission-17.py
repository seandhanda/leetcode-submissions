class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}
    #O(1) time
    #O(1) space

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.root.isEnd = True
    #O(1) time
    #O(1) space

    def addWord(self, word: str) -> None:
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
            return False
        
        curr = self.root

        # 2 MISTAKES:
        #1) dont return dfs immediately, rather we need to iterate across all iterations of the loop
        #2) dfs(i+1), not dfs(index+1)!!!!

        def dfs(index: int, curr: TrieNode) -> bool:
            for i in range(index,len(word),+1):
                if word[i] == ".":
                    for letter in curr.children:
                        if dfs(i+1, curr.children[letter]):
                            return True
                    return False
                elif word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]
            if curr.isEnd:
                return True
            else:
                return False    

        return dfs(0, curr)
    #O(L*k^2) time
    #O(L) space
