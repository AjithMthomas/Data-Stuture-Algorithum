class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedList:
    def __init__(self):
        self.head=None
#traversing through linked list
    def printLL(self):
        if self.head is None:
            print('empty linked list')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
LL=linkedList()
LL.printLL()
        