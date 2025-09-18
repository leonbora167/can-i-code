class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1        

    def print(self):
        temp = self.head 
        while(temp != None):
            print(temp.value)
            temp = temp.next 
        print("Length of linked list is ",self.length)

    def append_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node 
        self.length = self.length + 1
    
    def find_middle(self): #Without length of linked list given with 0(n) complexity
        slow = self.head 
        fast = self.head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next 
            fast = fast.next.next 
        print("Middle value is ",slow.value)


ll1 = LinkedList(2)

ll1.append_start(3)
ll1.append_start(22)
ll1.append_start(33)
ll1.append_start(54)
ll1.append_start(1)
ll1.append_start(100)

ll1.print()

ll1.find_middle()