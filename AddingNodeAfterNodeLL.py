class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if self.head is None:
            print('it is a empty List')
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.ref
    def Add_start(self,data):
        new_Node= Node(data)
        new_Node.ref = self.head
        self.head = new_Node
        
        
    def Add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print('there no given node in the linked list')
        else:
            new_node =Node(data)
            new_node.ref = n.ref
            n.ref = new_node
LL = LinkedList()
LL.Add_start(30)
LL.Add_start(40)
LL.Add_after(20,30)
LL.traverse()