class Node:
    def __init__ (self, value=None,parent=None,isRoot=False,isLeft=False,isRight=False):
        self.value = value
        self.right = None
        self.left = None
        self.parent = parent
        self.isRoot = isRoot
        self.isLeft = isLeft
        self.isRight = isRight