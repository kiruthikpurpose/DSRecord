class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def insertNode(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insertNode(root.left, data)
        else:
            root.right = self.insertNode(root.right, data)
        return root

    def inorderTraversal(self, node):
        if node is not None:
            self.inorderTraversal(node.left)
            print(node.data, end=" ")
            self.inorderTraversal(node.right)

if __name__ == '__main__':
    
    n = int(input())
    root_get = int(input())
    bst = BinarySearchTree(root_get)
    for i in range(n-1):
        data = int(input())
        bst.insertNode(bst.root, data)

    bst.inorderTraversal(bst.root)