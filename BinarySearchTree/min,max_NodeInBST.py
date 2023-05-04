class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insertion(self,data):
        if self.key is None:
            self.key = data
            return
        if data<self.key:
            if self.lchild:
                self.lchild.insertion(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insertion(data)
            else:
                self.rchild = BST(data)
    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key)
        if self.rchild:
            self.rchild.inOrder()
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print('smallest node is:',current.key   )
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("max node is:",current.key)

root = BST(10)
list1=[46,6,4,3,2,1]
for i in list1:
    root.insertion(i)
root.inOrder()
root.max_node()
root.min_node()