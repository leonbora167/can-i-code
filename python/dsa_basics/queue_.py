class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node 
        self.last = new_node 
        self.length = 1 

    def print(self):
        temp = self.first 
        while temp is not None:
            print(temp.value)
            temp = temp.next 
        print("Queue length is ", self.length)

    def enqueue(self, value): #Adding element at end of queue 
        new_node = Node(value)
        if self.first is None:
            self.first = new_node 
            self.last = new_node 
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self): #Remove an element from start of queue
        if self.length == 0:
            return "Queue Empty"
        temp = self.first 
        if self.length == 1:
            self.first = None 
            self.last = None 
        else:
            self.first = self.first.next 
            temp.next = None 
        self.length -= 1
        return temp


qu = Queue(3)
qu.enqueue(4)
qu.enqueue(5)
qu.print()
