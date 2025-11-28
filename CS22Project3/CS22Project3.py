####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Project 3 Homework Assignment
# Due Date: December 1 2025
####################################################
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_new_node(self, new_node):
        #insert first node if none are present
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            done_with_new_node = False

            while done_with_new_node != True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        done_with_new_node = True
                    #otherwise move temp to the left
                    temp = temp.left
                elif new_node.data > temp.data:
                    if temp.right is None:
                        temp.right = new_node
                        done_with_new_node = True
                    #otherwise move temp to the right
                    temp = temp.right
                else:
                    print(new_node.data, 'is already in the tree; Duplicates not allowed')
                    done_with_new_node = True

    #preorder: root -> left subtree -> right subtree
    def traverse_preorder(self, start_node):
        if start_node is not None:
            print(start_node.data, end=' ')
            self.traverse_preorder(start_node.left)
            self.traverse_preorder(start_node.right)

    #postorder: left subtree -> right subtree -> root
    def traverse_postorder(self, start_node):
        if start_node is not None:
            self.traverse_postorder(start_node.left)
            self.traverse_postorder(start_node.right)
            print(start_node.data, end=' ')

    #inorder: left subtree -> root -> right subtree
    def traverse_inorder(self, start_node):
        if start_node is not None:
            self.traverse_inorder(start_node.left)
            print(start_node.data, end=' ')
            self.traverse_inorder(start_node.right)

def main():
    bst = BinarySearchTree()
    
    #open file for reading
    with open('tree_values.txt', 'r') as proxy:
            for number in proxy:
                number = int(number.rstrip("\n"))
                bst.insert_new_node(Node(number))

    print('Preorder:', end='')
    bst.traverse_preorder(bst.root)
    print()

    print('Postoder:', end='')
    bst.traverse_postorder(bst.root)
    print()

    print('Inorder:', end='')
    bst.traverse_inorder(bst.root) 

main()
