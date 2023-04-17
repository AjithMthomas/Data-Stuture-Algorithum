class Node:
    def __init__(self,data):
        self.data = data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head = None
    def Traverse(self):
        if self.head is None:
            print('empty')
        else:
            n = self.head
            while n is not None:
               print(n.data)
               n = n.ref
    def add_Element(self,data):
        if self.head is None:
            newNode=Node(data)
            self.head = newNode
        else :
            print('not empty')
    
l=LinkedList()
l.add_Element(10)
l.add_Element(20)
l.Traverse()
                