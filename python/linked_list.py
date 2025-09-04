class Node: # Initializes a node with a value with it pointing to "nothing"
    def __init__(self, value):
        self.value = value 
        self.next = None 

class LinkedList: 
    def __init__(self, value): # Initializes a ll
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node 
        self.length = 1 

    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node 
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.length == 0:
            return None #Empty ll
        temp = self.head 
        pre = self.head 
        while(temp.next != None):
            pre = temp 
            temp = temp.next 
        self.tail = pre 
        self.tail.next = None 
        if(se)



linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()
linked_list.tail.net