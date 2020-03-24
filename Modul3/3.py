class Node():
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
#mencari data
def cari(head,x):
    cnode=head
    position=0
    while cnode is not None:
        position+=1
        if cnode.data == x:
            print(cnode.data," di posisi:",position)
            break
        else:
            cnode = cnode.next
class LinkedList:
    def __init__(self):
        self.head = None
# menambah data menjadi head
    def tambahHead(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
# menambah data menjadi tail
    def tambahAkhir(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
#mengahpus data
    def hapusNode(self, position):
        if self.head == None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position -1 ):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next
