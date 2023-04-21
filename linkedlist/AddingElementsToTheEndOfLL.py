class Node:
   def __init__(self,data):
      self.data = data
      self.ref = None

class LinkedList:
    def __init__(self):
      self.head = None
    def traverse(self):
       if self.head  is None:
           print('empty linked list')
       else :
          n = self.head
          while n is not None:
             print(n.data,"--->",end =" ")
             n = n.ref 
    def add_end(self,data):
       new_node = Node(data)
       if self.head is None:
          self.head = new_node
       else:
          n = self.head
          while n.ref is not None:
             n = n.ref
          n.ref = new_node

LL=LinkedList()
LL.add_end(30)
LL.add_end(40)
LL.traverse()

         
  
  
  
      
