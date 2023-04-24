class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def Traverse (self):
        if self.head is None:
            print('empty list')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_end(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                n =n.ref 
            n.ref=newNode
            

            
    def add_Before_node(self,data,x):
        if self.head is None:
            print('empy LINKED LIST')
            return
        
        if self.head.data == x:
            newNode = Node(data)
            newNode.ref = self.head
            self.head = newNode
            return
        n = self.head
        while n is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n is None:
            print("empty")
        else:
            newNode = Node(data)
            newNode.ref = n.ref
            n.ref = newNode


LL=LinkedList()
LL.add_end(20)
LL.add_Before_node(15,20)
LL.Traverse()