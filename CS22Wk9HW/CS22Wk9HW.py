####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 9 Homework Assignment
# Due Date: November 23 2025
####################################################

class MinHeap():
    def __init__(self):
        self.heap = []
        self.size = 0

    def get_left_child(self, index):
        return 2 * index + 1 

    def get_right_child(self, index):
        return 2 * index + 2

    def get_parent(self, index):
        return (index -1) // 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def remove_root(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            self.size -= 1
            return self.heap.pop()
        
        value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self.sink_down(0)

        return value

    def insert(self, value):
        self.heap.append(value)
        self.size += 1

        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self.get_parent(current)]:
            parent = self.get_parent(current)
            self.swap(current, parent)
            current = parent

    def sink_down(self, index):
        smallest = index

        while True:
            left = self.get_left_child(index)
            right = self.get_right_child(index)

            #check if left child exists
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            #check if right child exists
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            #if the smallest is not the parent, swap it
            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                return

def main():
    minheap = MinHeap()
    minheap.insert(99)
    minheap.insert(72)
    minheap.insert(61)
    minheap.insert(58)

    print(minheap.heap)

    minheap.insert(100)
    print('After inserting 100:', minheap.heap)

    minheap.insert(75)
    print('After inserting 75:', minheap.heap)

    minheap.remove_root()
    print('After removing root:', minheap.heap)

    minheap.remove_root()
    print('After removing root:', minheap.heap)


main()






        

