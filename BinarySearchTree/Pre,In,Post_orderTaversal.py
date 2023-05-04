class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if data<self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    def preOrder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preOrder()
        if self.rchild:
            self.rchild.preOrder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.key,end=" ")

    def min_node(self):
        current = self
        while current.lchild is not None:
            current = current.lchild
        print('current',current.key)


        

root = BST(10)
list1 = [2,35,5,3,45,32]
for i in list1:
    root.insert(i)

root.preOrder()
print('preorder')
root.inorder()
print('inorder')
root.postOrder()
print('postOrder')
root.min_node()


