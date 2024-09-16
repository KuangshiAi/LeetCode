class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode()
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy_head
        for i in range(index + 1):
            cur = cur.next
        return cur.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val=val)
        new_node.next = self.dummy_head.next
        self.dummy_head.next = new_node
        self.size += 1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur = self.dummy_head
        while cur.next:
            cur = cur.next
        new_node = ListNode(val=val)
        cur.next = new_node
        self.size += 1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        new_node = ListNode(val=val)
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        temp = cur.next
        cur.next = cur.next.next
        del temp
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)