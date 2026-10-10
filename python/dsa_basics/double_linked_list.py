class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None 

class DoubleLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node 
        self.tail = node 
        self.length  = 1

    def print(self):
        temp = self.head 
        while(temp is not None):
            print(temp.value)
            temp =temp.next
        print("Length of linked list is ", self.length)

    def append_end(self, value): # O(1)
        new_node = Node(value)
        if(self.head is None):
            self.head = Node 
            self.tail = Node 
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1 
        return True
    
    def pop_end(self): # O(1)
        if self.length == 1:
            self.head = None 
            self.tail = None 
            return self.value
        else:
            temp = self.head
            print("Popped value is ",self.tail.value)
            self.tail = self.tail.prev 
            self.tail.next = None
            self.length -= 1

    def append_beg(self, value): # O(1)
        new_node = Node(value)
        temp = self.head
        self.head.prev = new_node
        self.head = new_node
        self.head.next = temp 
        self.length = self.length + 1 

    def pop_first(self): #O(1)
        if self.length == 1:
            print("popped value is ", self.head.value)
            return "List over"
        else:
            print("Popped value is ", self.head.value)
            temp = self.head 
            self.head = self.head.next 
            self.head.prev = None 
            temp.next = None 
            self.length = self.length - 1

    def set_val(self, value, index): #Push old value towards left side
        new_node = Node(value)
        temp = self.head
        prev = temp
        if(index == 0):
            self.append_beg(value)
        elif(index == self.length - 1):
            self.append_end(value)
        else:
            for _ in range(index):
                pre = temp 
                temp = temp.next
            pre.next = new_node
            new_node.prev = pre 
            temp.pre = new_node
            new_node.next = temp 
            self.length += 1
        
    def remove_any(self, index):
        if(index == 0):
            self.pop_first()
        elif(index == self.length - 1):
            self.pop_end()
        else:
            temp = self.head
            pre = self.head
            for i in range(index):
                pre = temp
                temp = temp.next
            print("Removed value is ", temp.value)
            curr = temp.next
            pre.next = curr 
            curr.prev = pre 
            temp.next = None 
            temp.prev = None 
            self.length = self.length + 1 
            
            

dll = DoubleLinkedList(1)
dll.append_end(23)
dll.append_end(32)
dll.print()

dll.pop_end()
dll.append_beg(19)
dll.append_beg(24)

dll.pop_first()
dll.print()

dll.set_val(18, 1)
dll.print()

dll.remove_any(2)
dll.print()