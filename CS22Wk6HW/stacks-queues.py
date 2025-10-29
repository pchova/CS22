#queues in python
from collections import deque

q = []

#Enqueue (add elements to the queue)
q.append("sofa")
q.append("gem")
q.append("philya")
q.append("sofa again")

print(q)
print()

#Dequeue (remove elements)
first_pet = q.pop(0)
print(first_pet)
print(q)
print()

#collections module provide a deque (double ended queue) class,
#optimized for fast appends and pops from both ends
queue = deque()

#enqueue (add elements to the queue)
queue.append("mango")
queue.append("pineapple")
print(queue)
print()

#dequeue 
first_item = queue.popleft()
print(first_item)
print(queue)
print()

print("*******Python QUEUE class example******")
#using python class as a queue:
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.ifEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    #Peek returns the first element in the queue
    def peek(self):
        if self.ifEmpty():
            return 'Queue is empty'
        return self.queue[0]
    
    def ifEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

def main():
    myQ = Queue()
    myQ.enqueue('P')
    myQ.enqueue('O')
    myQ.enqueue('L')
    myQ.enqueue('I')
    myQ.enqueue('N')
    myQ.enqueue('A')

    print('Queue:', myQ.queue)
    print('Peek:', myQ.peek())
    print('Dequeue:', myQ.dequeue())
    print("Queue after dequeue:", myQ.queue)
    print("ifEmpty:", myQ.ifEmpty())
    print("Size:", myQ.size())

main()





