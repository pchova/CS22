####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 8 Homework Assignment
# Due Date: November 16 2025
####################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    #preorder: root -> left subtree -> right subtree
    def preorder(self, start_node):
        if start_node is not None:
            print(start_node.data, end=' ')
            self.preorder(start_node.left)
            self.preorder(start_node.right)

    #postorder: left subtree -> right subtree -> root
    def postorder(self, start_node):
        if start_node is not None:
            self.postorder(start_node.left)
            self.postorder(start_node.right)
            print(start_node.data, end=' ')

    #inorder: left subtree -> root -> right subtree
    def inorder(self, start_node):
        if start_node is not None:
            self.inorder(start_node.left)
            print(start_node.data, end=' ')
            self.inorder(start_node.right)

def main():
    bt = BinaryTree()

    #level 0 of binary tree
    bt.root = Node(1)

    #level 1 of binary tree
    bt.root.left = Node(2)
    bt.root.right = Node(3)

    #left side
    bt.root.left.left = Node(4)
    bt.root.left.left.left = Node(8)
    bt.root.left.left.right = Node(9)
    
    bt.root.left.right = Node(5)
    bt.root.left.right.left = Node(10)
    bt.root.left.right.right = Node(11)

    #right side
    bt.root.right.left = Node(6)
    bt.root.right.left.left = Node(12)
    bt.root.right.left.right = Node(13)

    bt.root.right.right = Node(7)
    bt.root.right.right.left = Node(14)
    bt.root.right.right.right = Node(15)

    print("Preorder Traversal:", end=' ')
    bt.preorder(bt.root)
    print()

    print("Postorder Traversal:", end=' ')
    bt.postorder(bt.root)
    print()

    print("Inorder traversal:", end=' ')
    bt.inorder(bt.root)
    print()

main()

    
