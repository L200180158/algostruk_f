class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def tambahawal(self, x):
        new = Node(x)
        new.next = self.head
        if self.head is not None:
            self.head.prev = new
        self.head = new
    def tambahakhir(self, x):
        new = Node(x)
        new.next = None
        if self.head is None:
            new.prev = None
            self.head = new
            return
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = new
        new.prev = last
        return
    def printList(self, node):
        print("\nDari Depan :")
        while(node is not None):
            print(" % d" %(node.data))
            last = node
            node = node.next
        print("\nDari Belakang :")
        while(last is not None):
            print(" % d" %(last.data))
            last = last.prev
