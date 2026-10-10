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

    def peek(self):
        print("Peeking")
        if self.height == 0:
            return "STack empty"
        else:
            print(self.top.value)
            return self.top.value
        
class Stack_List: #Ultimatley a list is a stack where elements are appended towards the end and the "top of stack" is the end of the list
    def __init__(self):
        self.stack = [] 
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def print_stack(self):
        print("Stack Top -> Bottom")
        for i in reversed(self.stack):
            print(i)
    def reverse(self):
        string = ''
        for i in reversed(self.stack):
            string = str(i) + string 
        print("Reversed string is ", string)
    def check_parantheses(self):
        temp_stack = Stack_List()
        for i in self.stack:
            if i == "(":
                temp_stack.push("(")
            elif i == ")":
                temp_stack.pop()
        if temp_stack.is_empty():
            print("Balanced")
        else:
            print("Not balanced")
    def sort(self):
        temp_stack = Stack_List()
        while not self.is_empty(): #While original stack is not empty
            temp = self.pop()
            if temp_stack.is_empty():
                temp_stack.push(temp)
            else:
                if temp < temp_stack.peek():
                    temp_stack.push(temp)
                elif temp > temp_stack.peek():
                    while True:
                        temp2 = temp_stack.pop()
                        self.push(temp2)
                        if temp_stack.is_empty() or temp < temp_stack.peek():
                            temp_stack.push(temp)
                            break
        print("Stack sorted from top (low) to bottom (high)")
        temp_stack.print_stack()

class queue_stack:
    def __init__(self):
        self.in_stack = Stack_List()
        self.out_stack = Stack_List()
    def enqueue(self, value):
        self.in_stack.push(value)
    def dequeue(self):
        if self.is_empty():
            return None 
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()
    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()
    # pushing into a stack - enqueue - [1, 2, 3]
    # taking out from stack - dequeue - [3, 2, 1] - hence the peek operation will give the last element 1 which theoretically as in a queue was the first element

stack = Stack(4)
stack.push(1)
stack.push(12)
stack.peek() 

pa = Stack_List()
pa.push("(")
pa.push(")")
pa.push("(")
pa.push(")")
pa.push("(")
pa.print_stack()
pa.check_parantheses()

sl = Stack_List()
sl.push(3)
sl.push(4)
sl.push(1)
sl.push(2)
#sl.print_stack()
#sl.reverse()
sl.sort()