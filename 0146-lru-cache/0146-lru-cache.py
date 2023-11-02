class Node:
    # Define dll
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity # length of the LRUcache
        self.cache = {}
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def insert(self, node):
        #insert a new node 
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def remove(self, node):
        #remove a node from ll
        nxt, prev = node.next, node.prev
        prev.next, nxt.prev = nxt, prev
        
    def get(self, key: int) -> int:
        #Get value and update it to the MRU
        if key in self.cache:
            self.remove(self.cache[key]) # remove from doubly linked list
            self.insert(self.cache[key]) # insert at the right
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) # create new node
        self.insert(self.cache[key]) # insert the new node
        
        # check if the capacity exceeds the cache capacity after inserting
        if len(self.cache) > self.capacity:
            # remove the LRU from hashmap and remove from the linked list
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)