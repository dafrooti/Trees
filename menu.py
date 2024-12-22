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

root = None


while True:
    print("Press 1 to make the root of a tree")
    print("Press 2 to make the root's children")
    print("Press 3 for inorder traversal")
    print("Press 4 for preorder traversal")
    print("Press 5 for postorder traversal")
    print("Press 6 to exit")

    choice = int(input("Enter option: "))

    if choice == 1:
        root = Tree(input("What root would you like: "))
        

    elif choice == 2:
        root.left = Tree(input("What would you like as the root's left child: "))
        root.right = Tree(input("What would you like as the root's right child: "))
        root.left.right = Tree(input("What would you like as the left node's right child: "))
        root.right.right = Tree(input("What would you like as the right node's right child: "))
        root.right.left = Tree(input("What would you like as the right node's left child: "))

    elif choice == 3:
        inorder_traversal(root)
    elif choice == 4:
        preorder_traversal(root)
    elif choice == 5:
        postorder_traversal(root)

    elif choice >= 6:
        break