class ListNode:
    def __init__(self, val = None, key = None):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {} # key : pointer to Linked List Node
        self.capacity = capacity
        self.LRU = ListNode()
        self.MRU = ListNode()
        
        #connect the linked list
        self.MRU.prev = self.LRU
        self.LRU.next = self.MRU

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        value = node.val

        #remove
        # prev = node.prev
        # prev.next = node.next
        self.remove(node)
        #insert
        # temp = LRU.next
        # node.prev = LRU
        # LRU.next = node
        # node.next = temp
        self.insert(node)
        
        return value

    def put(self, key: int, value: int) -> None:
        if len(self.map) == self.capacity and key not in self.map:
            node = self.LRU.next
            self.remove(node)
            nodeKey = node.key
            del self.map[nodeKey]
        if key in self.map:
            self.remove(self.map[key])
            del self.map[key]
        
        self.map[key] = ListNode(value, key)
        self.insert(self.map[key])


    def remove(self, node: ListNode) -> None:
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

    def insert(self, node: ListNode)-> None:
        temp = self.MRU.prev
        node.next = self.MRU
        node.prev = temp
        self.MRU.prev = node
        temp.next = node
        
