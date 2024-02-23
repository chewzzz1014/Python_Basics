class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def inOrder(root):
    if root is None:
        print("")
    else:
        if root.left is not None:
            inOrder(root.left)
        print(root.info, end=" ")
        if root.right is not None:
            inOrder(root.right)


def preOrder(root):
    if root is None:
        print("")
    else:
        print(root.info, end=" ")
        if root.left is not None:
            preOrder(root.left)
        if root.right is not None:
            preOrder(root.right)


def postOrder(root):
    if root is None:
        print("")
    else:
        if root.left is not None:
            postOrder(root.left)
        if root.right is not None:
            postOrder(root.right)
        print(root.info, end=" ")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

postOrder(tree.root)