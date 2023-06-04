# becasue heap is a complete binary tree, so we can use array to represent it
# WeRide VOE
# TC: insert O(logn) pop O(logn)  SC: O(n)
class Heap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap)-1)
    
    def pop(self):
        self.swap(0, len(self.heap)-1) # swap the root and the last element
        value = self.heap.pop() # remove the last element
        self.sift_down(0)
        return value
    
    def sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def sift_down(self, i):
        while True:
            left = self.left_child(i)
            right = self.right_child(i)
            smallest = i
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.swap(i, smallest)
            i = smallest

heap = Heap()
heap.insert(1)
heap.insert(3)
heap.insert(2)
print(heap.pop()) # 1
heap.insert(-1)
heap.insert(4)
print(heap.pop()) # -1
print(heap.pop()) # 2
print(heap.pop()) # 3
print(heap.pop()) # 4
