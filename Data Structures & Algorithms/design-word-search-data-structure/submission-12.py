import string

class TrieNode:
    def __init__(self):
        self.children = {} 
        self.isEnd = False


class WordDictionary:
#WRONG IDEA: because of the . wildcard! 
# Just a map!
# Trie, unecessary because we dont need prefix functionality
    
# Instead we use Trie to handle wildcard
    
    def __init__(self):
        self.root = TrieNode()
        # self.root.isEnd = True
    #O() time
    #O() space    

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    #O(L) time
    #O(L) space


#WHY RECURSION: 1) We need to evaluate multiple branches (THIS IS IT) 2) Without helper, we initialize curr to root each iteration! Instead initialize through passing in caller and then set curr to argument of helper in helper
    def search(self, word: str) -> bool:
        
        def dfs(root: Optional[TrieNode], index: int) -> bool:
            curr = root
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for letter in curr.children:
                    # for letter in string.ascii_lowercase:
                        if dfs(curr.children[letter], i + 1):
                            return True 
                    return False
                if c not in curr.children:
                    return False
                curr = curr.children[c]
            if curr.isEnd:
                return True
            else:
                return False
        
        return dfs(self.root, 0)


    #O(L * K^2) time
    #O(L) space

# #SEARCH NOTE VERY IMPORTANT TO UNDERSTANDING WHY WE NEEDED HELPER:
# my original implementaiton of recursion that did not use a helper required a helper for ONE REASON only - to allow us to initalize root outside helper such that curr is not reset to root each time. There was no other reason, and if this was not an issue, we would not need a helper because return type and argument is the same (technically we could just pass in a pruned version of word instead of index so that the stubs match at the cost of space complexity.