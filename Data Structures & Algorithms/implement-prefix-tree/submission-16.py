# We use tries for prefix searches, which hashmap cannot do in O(L) time, instead in O(n) time
# Checking if any word in our dictionary starts with XX, would take O(n) with hashmap (iterating across every item and checking their first 2 characters), but with Trie its O(L) 

# Binary Tree Implementation via just TreeNode - functions will be implemented in internal class like solution
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# --Binary Tree Class Implementation
# class TreeNode:
#     def __init__(self, val: int = 0):
#         self.val = val
#         self.left = None
#         self.right = None        

# class BinaryTree:
#     def __init__(self, root: Optional[TreeNode] = None):
#         self.root = root
# --Binary Tree Class Implementation Fini --


class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}
    # O(1) time
    # O(1) space, and EVENTUALLY its worst case space will be O(k) where k is min(26, number of words in trie with unique letter at that position)


#PrefixTree starts at root which is just a placeholder node that maps the first character of any string
#At any node, does child map contain the character of the next character we want (at root, this means does it have the first character of the string)
class PrefixTree:

    # def__init(self, root: Optional[TrieNode] = None):
        # self.root = root

    def __init__(self):
        self.root = TrieNode()
    #O(1) time
    #O(1) space, eventually worst case size becomes O(k) where k is min(26, number of unique letter at that position across all words in the trie)
            

    def insert(self, word: str) -> None:
        # curr = self.root
        # for i in range(len(word)):
        #     if word[i] in curr.children:
        #         node = curr.children[word[i]]
        #         if i == len(word) - 1:
        #             node.isEnd = True
        #     else: 
        #         node = TrieNode()
        #         if i == len(word) - 1:
        #             node.isEnd = True
        #         curr.children[word[i]] = node 
        #     curr = node
        # curr.isEnd = True
        # #O(L) space
        # #O(L) time

        #cleaner (same complexities):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
        #O(L) space
        #O(L) time



    def search(self, word: str) -> bool:
        i = 0
        curr = self.root
        while i < len(word):
            if word[i] not in curr.children:
                return False
            else:
                curr = curr.children[word[i]]
                i += 1
        
        if curr.isEnd:
            return True

        return False   
    #O(L) time
    #O(1) space 

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.children:
                return False
            else:
                curr = curr.children[prefix[i]]
        return True
        #O(1) space
        #O(L) time
        
  
    