class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
   
    def add_begin(self,data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head = newNode
    def Traverse(self):
        if self.head is None:
            print("empty linked List")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n = n.ref
LL=LinkedList()
l=[1,2,3,4,5,6,]
for i in l:
    LL.add_begin(i)

LL.Traverse()



    
