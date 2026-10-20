class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    #O(1) space
    #O(1) time


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)
        self.cache = {}

        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
        

    #O(1) time
    #O(n) space


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].value

    #O(1) space
    #O(1) time

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    #O(1) space
    #O(1) time

    def insert(self, node: Node):
        node.next = self.MRU
        node.prev = self.MRU.prev
        self.MRU.prev.next = node
        self.MRU.prev = node

    #O(1) space
    #O(1) time

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity and key not in self.cache:
            node = self.LRU.next
            self.remove(node)
            del self.cache[node.key]
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        return

    #O(1) space
    #O(1) time

# class Node:
#     def __init__(self, key: int, val: int, prev = None, next = None):
#         self.key = key
        
#         self.val = val
#         self.prev = prev
#         self.next = next

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.LRU = Node(0,0)
#         self.MRU = Node(0,0)
#         self.LRU.next = self.MRU
#         self.MRU.prev = self.LRU
#         self.cache = {}


#     def get(self, key: int) -> int:
#         if key in self.cache:
#             node = self.cache[key]

#             node.prev.next = node.next
#             node.next.prev = node.prev

#             node.next = self.MRU
#             node.prev = self.MRU.prev
#             node.prev.next = node
#             self.MRU.prev = node
#             return self.cache[key].val
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if len(self.cache) >= self.capacity and key not in self.cache:
#             leastUsed = self.LRU.next
#             del self.cache[leastUsed.key]
#             self.LRU.next = self.LRU.next.next
#             self.LRU.next.prev = self.LRU

#         if key in self.cache: #you can either update the node, and move it to MRU, and then return OR just remove the node from linked list and allow below to create new node (as if it were update)
#             prevNode = self.cache[key].prev
#             nextNode = self.cache[key].next
#             nextNode.prev = prevNode
#             prevNode.next = nextNode


            

#         #not updating, new node (no need to remove from current position and place in MRU, just place in MRU)
#         self.cache[key] = Node(key, value)
#         node = self.cache[key]

#         node.next = self.MRU
#         node.prev = self.MRU.prev
#         self.MRU.prev = node
#         node.prev.next = node

#         return