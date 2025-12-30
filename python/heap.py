class MaxHeap:
    def __init__(self):
        self.heap = [] 

    def left_child(self, index):
        return 2*index + 1 
    
    def right_child(self, index):
        return 2*index + 2 
    
    def parent(self, index):
        return (index-1)//2 
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1] 
        return True 
    
    def insert(self, value): #Max Heap by default does no gurantee order -> Every parent node is greater than its children is the condition
        self.heap.append(value) #Append value at end of list then check if the positioning is correct or not 
        current = len(self.heap) - 1 
        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        return True 
    
    def remove(self):
        if len(self.heap) == 0:
            return None 
        if len(self.heap) == 1:
            return 
        
    def sink_down(self, index): #Checks if the index node (parent ) satisifies the max condition 
        max_index = index 
        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            if(left_index < len(self.heap)) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index 
            
            if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index 
            
            if max_index != index:
                self.swap(index, max_index)
                index = max_index
            else:
                return 
            
    def remove(self): #Remove max top value from heap
        if (len(self.heap) == 0):
            return None 
        
        if len(self.heap) == 1:
            return self.heap.pop() 
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop() #Last element and replacing the head of heap with this 
        self.sink_down(0) #Re arranging the last element wrt to the other elements from top 

        return max_value
    
    def k_th_smallest(self, arr, k):
        heap = MaxHeap() 
        for i in arr:
            heap.insert(i)

            if(len(heap.heap) > k):
                heap.remove() # Whenever number of elements in heap exceeds 'k' we ll remove the max element
        # Now you should be left with a heap of k-elements and they shold be the k smallest ones from array

        kth_smallest = heap.heap[0] # For examples if 7-4-3 is the heap then the top(max) is the 3rd smallest rt
        return kth_smallest
    
    def max_stream(self, stream): # When a stream of elements is being sent, you should be able to determine which element is the maximum every time
        heap = MaxHeap() 
        for index, i in enumerate(stream):
            heap.insert(i)
            print(f"Current maximum for element {index} is {heap.heap[0]}")
        return True 
        
        


heap = MaxHeap()
heap.insert(99)
heap.insert(61)
heap.insert(52)
heap.insert(72)
heap.insert(55)

print(heap.heap)

heap.remove()
print(heap.heap)

arr = [20,15,10,4,3,7]
k = 3
print("Kth smallest ",heap.k_th_smallest(arr, k))

heap.max_stream([20,15,10,4,30,3,7])