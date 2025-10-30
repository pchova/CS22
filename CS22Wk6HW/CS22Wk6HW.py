####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 6 Homework Assignment
# Due Date: November 2 2025
####################################################

# ---- ArrayStack() class ----
class ArrayStack():
    def __init__(self):
        self.__stack = []
        self.__size = 0

    def get_stack(self):
        return self.__stack
    
    def get_size(self):
        return self.__size
    
    def push(self, e):
        self.__stack.append(e)
        self.__size += 1
    
    def is_empty(self):
        return len(self.__stack) == 0

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        else:
            val = self.__stack[-1]
            del self.__stack[-1]
            self.__size -= 1
            return val

# ---- ArrayQueue() class ----
class ArrayQueue():
    def __init__(self):
        self.__data = []
        self.__size = 0

    def get_queue(self):
        return self.__data

    def get_size(self):
        return self.__size
    
    def is_empty(self):
        return self.__size == 0
    
    def first(self):
        if self.is_empty():
            return 'Queue is empty'
        return self.__data[0]
    
    #elements removed from the bottom of the stack (first element in list)
    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        else:
            val = self.__data[0]
            del self.__data[0]
            self.__size -= 1
            return val
    
    #element added to the beginning of the stack (last element in list)
    def enqueue(self, e):
        self.__data.append(e)
        self.__size += 1

# ---- Main Program ----      
def main():
    #Calls for ArrayStack class
    S = ArrayStack()
    S.push(20)
    S.push(43)
    S.push(15)
    print('S =', S.get_stack())
    print('Size of S =', S.get_size())
    print('Pop =', S.pop())
    print('Pop =', S.pop()) 
    print('S =', S.get_stack())
    print('Size of S =', S.get_size())
    S.push(55)
    print('S =', S.get_stack())
    print('Size of S =', S.get_size())

    print('Pop =', S.pop())
    print('Pop =', S.pop())
    print('S =', S.get_stack())
    print('Size of S =', S.get_size())
    print('Pop =', S.pop())
    print()

    #Calls for QueueStack class
    Q = ArrayQueue()
    Q.enqueue(44)
    Q.enqueue(33)
    Q.enqueue(77)
    print('Q =', Q.get_queue())
    print('Size of Q =',Q.get_size())
    print('DQ =', Q.dequeue())
    print('DQ =', Q.dequeue())
    print('Q =', Q.get_queue())
    print('Size of Q =', Q.get_size())
    Q.enqueue(11)
    print('Q =', Q.get_queue())
    print('Size of Q =', Q.get_size())
    print('DQ =', Q.dequeue())
    print('DQ =', Q.dequeue())
    print('Q =', Q.get_queue())
    print('Size of Q =', Q.get_size())
    print('DQ =', Q.dequeue())

main()
