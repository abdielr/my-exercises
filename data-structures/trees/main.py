from tree import BinarySearchTree

tree = BinarySearchTree()

tree.add(8)
tree.add(10)
tree.add(3)
tree.add(14)
tree.add(13)
tree.add(1)
tree.add(6)
tree.add(4)
tree.add(7)

tree.inOrder(tree.root)
tree.preOrder(tree.root)
tree.posOrder(tree.root)
print(tree.search(tree.root, 8) is not None)

