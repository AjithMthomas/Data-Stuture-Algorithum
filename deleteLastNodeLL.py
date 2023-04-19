class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def Traverse (self):
        if self.head is None:
            print('LL empty')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_start(self,data):
        node = Node(data)
        node.ref = self.head
        self.head = node
    def delete_end(self):
        if self.head is None:
            print('nouthing to delete')
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
LL=LinkedList()
LL.add_start(60)
LL.add_start(50)
LL.add_start(40)
LL.delete_end()
LL.Traverse()


