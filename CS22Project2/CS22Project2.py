####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Project 2 Homework Assignment
# Due Date: November 17 2025
####################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

# Function insert_at_head() places a node at the beginning of the list
    def insert_at_head(self, data):
        #creates a node using the parameter
        new_node = Node(data)

        #if head is none, both head and tail should be set to the new node
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
            new_node.next = new_node
        #else, the new node should be inserted at the head of the list, AND
        #the tail's next field should point to head
        else:
            new_node.next = self.__head
            self.__head = new_node
            self.__tail.next = self.__head

        #increases the size by 1
        self.__size += 1
    
    def insert_at_tail(self, data):
        #creates a node using the parameter 
        new_node = Node(data)

        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
            new_node.next = new_node
        else:
            #old tail points to the new node
            self.__tail.next = new_node
            #new node points to head
            new_node.next = self.__head
            #tail should now be the new node
            self.__tail = new_node

        #increases the size by 1
        self.__size += 1

    def remove_from_head(self):
        #remove a node at the beginning of the list

        #decrease size by 1
        self.__size -= 1

        #return the data field of the node that was removed

    def remove_from_tail(self):
        #remove a node at the end of the list

        #decrease size by 1
        self.__size -= 1

        #return the data field of the node that was removed

    def display(self):
        if self.__head == None:
            print('List is empty')
        else:
            temp = self.__head
            print('Here is your list:', end=' ')
            while temp is not None:
                print(temp.data, end=' ')
            print()



