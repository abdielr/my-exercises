from node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def empty(self):
        if self.root == None:
            return True
        else:
            return False
    def add(self,value):
        if self.empty():
            self.root = Node(value=value,isRoot=True)
        else:
            node = self.__getPlace(value)
            if value <= node.value:
                node.left = Node(value=value,parent=node,isLeft=True)
            else: 
                node.right = Node(value = value,parent=node,isRight=True)
    def __getPlace(self,value):
        aux = self.root 
        while aux is not None:
            temp = aux
            if value <= aux.value:
                aux = aux.left
            else:
                aux = aux.right
        return temp
    def inOrder(self, node):
        #left root right
        if node:
            self.inOrder(node.left)
            print(node.value)
            self.inOrder(node.right)
    def posOrder(self,node):
        #left right root
        if node:
            self.inOrder(node.left)
            self.inOrder(node.right)
            print(node.value)
            
    def preOrder(self,node):
        #root left right
        if node:
            print(node.value)
            self.inOrder(node.left)
            self.inOrder(node.right)
    def search(self,node,value):
        if node == None:
            return None
        else:
            if node.value == value:
                return node
            elif value <= node.value:
                return self.search(node.left,value)
            else:
                return self.search(node.right,value)       

            
