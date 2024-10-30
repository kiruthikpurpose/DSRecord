class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def insertNode(self, data):
        new_node = Node(data)
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp.left is None:
                temp.left = new_node
                break
            else:
                queue.append(temp.left)
            
            if temp.right is None:
                temp.right = new_node
                break
            else:
                queue.append(temp.right)

if __name__ == '__main__':
    root_element = int(input())
    tree_try = BinaryTree(root_element)
    n = list(map(int, input().split()))
    for i in range(len(n)):
        tree_try.insertNode(n[i])
    print("Tree structure successfully built!")