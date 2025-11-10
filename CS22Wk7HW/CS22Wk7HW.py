####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 7 Homework Assignment
# Due Date: November 9 2025
####################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.__size = 0
        self.__head = None

    def display_stack(self):
        if self.__size == 0:
            print('Stack is empty')
        else:
            temp = self.__head
            print('Here is your stack:', end=' ')
            while temp:
                print(temp.data, end=' ')
                temp = temp.next
            print()
    
    def push(self, value):
        new_node = Node(value)
        #add node to the beginning of the linked list
        new_node.next = self.__head
        self.__head = new_node
        #increase the size variable by 1
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            print('Stack is empty')
        else:
            #create a variable temp and set it equal to head
            temp = self.__head
            #using temp variable, move head to the next node in the stack
            self.__head = temp.next
            #and set temp.next to None
            temp.next = None
            #decreate size by 1
            self.__size -= 1
            #return temp.data
            return temp.data

class QueueLL:
    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None
    
    def display_queue(self):
        if self.__size == 0:
            print('Queue is empty')
        else:
            temp = self.__head
            print('Here is your queue:', end=' ')
            while temp is not None:
                print(temp.data, end=' ')
                temp = temp.next
            print()

    def enqueue(self, data):
        new_node = Node(data)
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1
    
    def dequeue(self):
        if self.__size == 0:
            return 'Queue is empty'
        else:
            #create variable temp and set it equal to head
            temp = self.__head
            #using temp var, move head to the next node in the stack
            self.__head = temp.next
            #set temp.next to None
            temp.next = None
            #decrease size by 1
            self.__size -= 1
            return temp.data


def main():
    #Function calls for StackLL class
    S = StackLL()
    S.push(22)
    S.push(33)
    S.push(44)
    S.display_stack()
    print('Value popped:', S.pop())
    print('Value popped:', S.pop())
    S.display_stack()
    S.push(11)
    S.display_stack()
    print('Value popped:', S.pop())
    print('Value popped:', S.pop())
    S.display_stack()
    print()

    #Function calls for QueueLL class
    Q = QueueLL()
    Q.enqueue(66)
    Q.enqueue(77)
    Q.enqueue(88)
    Q.display_queue()
    print('Value dequeued:', Q.dequeue())
    print('Value dequeued:', Q.dequeue())
    Q.display_queue()
    Q.enqueue(99)
    Q.display_queue()
    print('Value dequeued:', Q.dequeue())
    print('Value dequeued:', Q.dequeue())
    Q.display_queue()

main()