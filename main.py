class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def display(self):
        print(self.value, self.left, self.right)

def inorder_traversal(root):
    if root.left != None:
        inorder_traversal(root.left)
    print(root.value)
    if root.right != None:
        inorder_traversal(root.right)

def preorder_traversal(root):
    print(root.value)
    if root.left != None:
        preorder_traversal(root.left)
    if root.right != None:
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root.left != None:
        postorder_traversal(root.left)
    if root.right != None:
        postorder_traversal(root.right)
    print(root.value)

root = Tree(6)
root.left = Tree(2)
root.right = Tree(7)
root.left.right = Tree(9)
root.right.right = Tree(37)
root.right.left = Tree(27)

inorder_traversal(root)
preorder_traversal(root)
postorder_traversal(root)