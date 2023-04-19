class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def Traverse(self):
        if self.head is None:
            print("empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_before(self,data,x):
        if self.head is None:
            print('L empty')
            return
        if self.head.data == x:
            node = Node(data)
            node.ref = self.head
            self.head = node
            return
        n = self.head
        while n is not None:
            if n.ref.data == x:
                break
            n = n.ref 
        if n is None:   
            print('empty')
        else:
            node = Node(data)
            node.ref = n.ref
            n.ref = node
    def add_first(self,data):
        v=node =Node(data)
        node.ref = self.head
        self.head = node
       
      
    def delete_FirstNode(self):
        n = self.head
        if n is None:
            print('empty')
        else:
            self.head = n.ref 

LL=LinkedList()
LL.add_first(20)
LL.add_first(15)
LL.add_before( 10,15)
LL.delete_FirstNode()
LL.Traverse()