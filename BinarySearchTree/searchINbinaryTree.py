class BST:
    def __init__(self,key) :
        self.key = key
        self.lchild = None
        self.rchild = None
    def Insertion(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.Insertion(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.Insertion(data)
            else:
                self.rchild = BST(data)
    def search(self,data):
        if self.key == data:
            print('value found')
            return
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('value not found')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('not found')

root = BST(10)
list1=[1,3,4,5,7,8,8]
for i in list1:
    root.Insertion(i)
root.search(10)