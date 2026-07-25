class DoubleLinkedList:
    def __init__(self,val,key,nxt=None,prev=None):
        self.val = val
        self.key = key
        self.nxt = nxt
        self.prev = prev

class LRUCache:
    # get and put in O(1) means it's hashMap
    # double linked list to maintain the order of the hashmap value which will be node
    # whenever a put operation is performed, it's checked against existing dictionary.
    # if the key exist update the dict, and move the node to first
    # if doesn't exist remove the last node in a linked list
    # keep tail and head node in handy to perform the operation much faster\
    def insertNode(self,key,val):
        # It always insert node at head
        node = DoubleLinkedList(val=val,key=key,nxt=self.head,prev=None)
        if self.head!=None:
            self.head.prev = node
        # if it's first node
        if self.tail==None:
            self.tail = node
        self.head = node
        self.cache[key] = self.head

    def deleteNode(self,):
        # it should always delete the tail node
        del_node = self.tail
        if del_node!=self.head:
            del_node.prev.nxt = None
        self.tail = del_node.prev
        del_node.prev = None
        del self.cache[del_node.key]

    def setAsHead(self,key):
        node = self.cache[key]
        if node==self.head:
            return
        node.prev.nxt = node.nxt
        if node!=self.tail:
            node.nxt.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = None
        node.nxt =self.head
        node.nxt.prev=node

        self.head = node


    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.setAsHead(key)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.setAsHead(key)
        elif len(self.cache) < self.capacity:
            self.insertNode(key,value)
        else:
            # capacity reached
            self.deleteNode()
            self.insertNode(key,value)
        