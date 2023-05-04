class BST:
    def __init__(self,key) :
        self.key = key
        self.lchild = None
        self.rchild = None
    def insertion(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key== data:
            return
        if self.key > data:
             if self.lchild:
                 self.lchild.insertion(data)
             else:
                 self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insertion(data)
            else:
                self.rchild = BST(data)
root=BST(None)
list1=[10,93,9,33,9,3]
for i in list1:
    root.insertion(i)

