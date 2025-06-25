class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev=None
        self.next=None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache={}
        self.oldest = Node(0,0)
        self.latest = Node(0,0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest
    
    def delete(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        del node
    
    def insert(self, node):
        prev = self.latest.prev
        prev.next = self.latest.prev = node
        node.prev = prev
        node.next = self.latest

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache.keys():
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.val
        else:
            return -1

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            del self.cache[lru.key]
            self.delete(lru)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)