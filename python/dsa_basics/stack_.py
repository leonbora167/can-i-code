class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1 

    def print(self):
        temp = self.top 
        while temp is not None:
            print(temp.value)
            temp = temp.next 
        print("Length of the stack is ", self.height)

    def push(self, value): # add an element at top of the stack
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top 
            self.top = new_node 
        self.height = self.height + 1 

    def pop(self): #Remove element from top of the stack
        if self.height == 0:
            return "Stack over - no pop possible"
        else:
            print("Popping element ", self.top.value)
            temp = self.top 
            self.top = self.top.next 
            self.height = self.height - 1
            temp.next = None #Imp to remove from memory

stack = Stack(4)
stack.push(1)
stack.push(12)
stack.print() 
stack.pop()
stack.print()