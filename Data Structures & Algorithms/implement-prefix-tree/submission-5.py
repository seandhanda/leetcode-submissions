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
    # O(k) space


#PrefixTree starts at root which is just a placeholder node that maps the first character of any string
#At any node, does child map contain the character of the next character we want (at root, this means does it have the first character of the string)
class PrefixTree:

    # def__init(self, root: Optional[TrieNode] = None):
        # self.root = root

    def __init__(self):
        self.root = TrieNode()
            

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr.children:
                node = curr.children[word[i]]
                if i == len(word) - 1:
                    node.isEnd = True
            else: 
                node = TrieNode()
                if i == len(word) - 1:
                    node.isEnd = True
                curr.children[word[i]] = node 
            curr = node
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
        
  
    