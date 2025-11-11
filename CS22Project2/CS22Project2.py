####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Project 2 Homework Assignment
# Due Date: November 17 2025
####################################################

class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None
    
class CircularLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def insert_at_head(self, data):
        #creates a node using the parameter data
        new_node = Node(data)
        #places the node at the beginning of the list
        #increases the size by 1
    

