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
        else:
            #new node points to current head
            new_node.next = self.__head
            #head should now be the new node
            self.__head = new_node
            #tail will point to the new node
            self.__tail.next = self.__head

        #increase size by 1
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
            #tail should now be the new node
            self.__tail = new_node
            #new node points to head
            new_node.next = self.__head

        #increase size by 1
        self.__size += 1

    def remove_from_head(self):
        #set temp to head
        temp = self.__head
        removed_data = temp.data

        #if temp.next is None, set both and tail to none
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            #set head to the next node
            self.__head = temp.next

            #if head.next equals tail, set tail.next to None 
            if self.__head == self.__tail:
                self.__tail.next = self.__head
            else:
                #otherwise set tail.next to head
                self.__tail.next = self.__head

        #set temp.next to None
        temp.next = None
        
        self.__size -= 1
        return removed_data

    def remove_from_tail(self):
        #set temp equal to head
        temp = self.__head
        prev = None

        removed_data = temp.data

        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            #move temp to the last node
            while temp.next != self.__head:
                prev = temp
                temp = temp.next

            #now - temp is the last node
            # prev is the node before temp
            removed_data = temp.data

            # set tail to prev after the loop
            self.__tail = prev

            if self.__tail == self.__head:
                self.__tail.next = self.__head
            else:
                self.__tail.next = self.__head

            temp.next = None

        self.__size -= 1
        return removed_data


    def display(self):
        if self.__head == None:
            print('List is empty')
        else:
            temp = self.__head
            print('Here is your list:', end=' ')

            print(temp.data, end=' ')
            temp = temp.next

            while temp != self.__head:
                print(temp.data, end=' ')
                temp = temp.next
                
            print()

def main():
    CLL = CircularLinkedList()
    CLL.insert_at_tail(10)
    CLL.insert_at_tail(20)
    CLL.display()
    CLL.insert_at_tail(30)
    CLL.display()
    CLL.insert_at_head(5)
    CLL.display()
    CLL.insert_at_head(1)
    CLL.display()
    print()

    print("Removed", CLL.remove_from_head(), "from head of the list")
    CLL.display()
    print()

    print("Removed", CLL.remove_from_head(), "from head of the list")
    CLL.display()
    print()

    print("Removed", CLL.remove_from_tail(), "from tail of the list")
    CLL.display()
    print()

    print("Removed", CLL.remove_from_tail(), "from tail of the list")
    CLL.display()
    print()

    print("Removed", CLL.remove_from_tail(), "from tail of the list")
    CLL.display()
    print()

main()



