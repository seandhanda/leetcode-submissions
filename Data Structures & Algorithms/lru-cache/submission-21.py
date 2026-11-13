class ListNode:
    def __init__(self, key = 0, val = 0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.LRU = ListNode()
        self.MRU = ListNode()
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            self.remove(key)
            self.insert(key)
            return self.map[key].val


    def put(self, key: int, value: int) -> None:
        if len(self.map) == self.capacity and key not in self.map:
            node = self.LRU.next
            self.remove(node.key)
            del self.map[node.key]
        if key in self.map:
            self.remove(key)
        self.map[key] = ListNode(key, value)
        self.insert(key)
        

    def remove(self, key: int) -> None:
        node = self.map[key]
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        return

    def insert(self, key: int) -> None:
        node = self.map[key]
        temp = self.MRU.prev
        self.MRU.prev = node
        node.next = self.MRU
        node.prev = temp
        temp.next = node


            
