# node class to contain the data like 2 pointers, key, value, to create a new node 
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None    # since a new node is not connected to anything yet
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity    # capacity of our cache
        self.map = {}
        self.head = Node(0, 0)      # dummy node
        self.tail = Node(0, 0)      # dummy node

        self.head.next = self.tail      # conneting head and tail for the cache since no in between nodes exist yet
        self.tail.prev = self.head

    def _remove(self, node): # to remove any node from the chain by making its neighbors point to each other instead
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_front(self, node):    # inserts the recently visited node at front
          first_node = self.head.next
          self.head.next = node
          node.prev = self.head
          node.next = first_node
          first_node.prev = node

    def get(self, key):
        if key not in self.map:
            return -1
        self._remove(self.map[key])   # self.map[key] gives node
        self._insert_front(self.map[key])    # insert at front
        return self.map[key].value
    
    def put(self, key, value):
        if key in self.map:
            self.map[key].value = value
            self._remove(self.map[key])   # remove before inserting to avoid duplicates in the chain
            self._insert_front(self.map[key])
            
        else:
            new_node = Node(key, value)
            self._insert_front(new_node)
            self.map[key] = new_node

        if len(self.map) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.map[lru_node.key]           # or we can use self.map.pop(lru_code.key) to remove from dict ie. map


## test cases
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # expected: 1
cache.put(3, 3)        # evicts key 2
print(cache.get(2))    # expected: -1
cache.put(4, 4)        # evicts key 1
print(cache.get(1))    # expected: -1
print(cache.get(3))    # expected: 3
print(cache.get(4))    # expected: 4
