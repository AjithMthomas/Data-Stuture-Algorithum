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

    def deleteAny(self,x):
        if self.head is None:
            print('empty')
            return
    
        if self.head.data==x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print('empty')
        else:
            n.ref = n.ref.ref
LL=LinkedList()
LL.add_start(10)
LL.add_start(9)
LL.add_start(8)
LL.deleteAny(9)
LL.Traverse()
