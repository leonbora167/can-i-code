class Node: #This class ll set the object with a value and it pointing to None as an individual node
    def __init__(self, value):
        self.value = value 
        self.next = None   

class LinkedList:
    def __init__(self, value): #First time class is called, it ll intitalize the new LL with a single node, for that object after that this constructor aint getting called again so no need to do anything here
        node = Node(value)
        self.head = node 
        self.tail = node
        self.length = 1

    def print(self):
        temp = self.head 
        while(temp is not None):
            print(temp.value)
            temp = temp.next 
        print("Length of the linked list is :", self.length)

    def append_end(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else: #If linked list is there we know the end "tail" so the Big O -> O(1)
            self.tail.next = new_node 
            self.tail = new_node
            self.length = self.length + 1
    
    def append_first(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
            self.length = 1 
        else: #We knw the head ; O(1)
            new_node.next = self.head
            self.head = new_node
            self.length = self.length + 1

    def pop_end(self):
        if(self.length == 0):
            return "Linked List has ended \ Error"
        else: #We have to travel to end -> O(n)
            temp = self.head
            pre = self.head
            while(temp != self.tail):
                pre = temp 
                temp = temp.next 
            print("Popped value is ", temp.value)
            pre.next = None 
            self.tail = pre
            self.length = self.length - 1

    def pop_first(self): #just change head -> O(1)
        print("Popped value is ", self.head.value)
        self.head = self.head.next 
        self.length = self.length - 1

    def get_val(self, index):
        # might have to go till the last index so -> O(n)
        if index == 0:
            val = self.head.value
            print(f"Value of index : {index} is : {val}")
        else:
            temp = self.head 
            counter = 0
            while(counter != index):
                counter = counter + 1
                temp = temp.next 
            else:
                val = temp.value
                print(f"Value of index : {index} is : {val}")

    def replace_val(self, value, index): # O(n)
        if(index <0 or index >= self.length):
            print("Error out of bounds index")
        new_node = Node(value)
        if index == 0: #First element
            new_node.next = self.head.next 
            self.head = new_node
        elif index == (self.length-1): #Last element
            temp = self.head 
            while(temp != self.tail):
                pre = temp 
                temp = temp.next 
            pre.next = new_node
            self.tail = new_node
        else: #Any random index
            temp = self.head 
            pre = self.head
            counter = 0 
            while(counter != index):
                pre = temp 
                temp = temp.next
                counter = counter + 1
            pre.next = new_node 
            new_node.next = temp.next

    def remove_any(self, index):
        if(index <0 or index >= self.length):
            print("Out of Bounds")
        if(index == 0): #At head
            self.head = self.head.next 
            self.length = self.length - 1 
        elif(index == self.length-1): #AT tail
            temp = self.head 
            pre = self.head 
            while(temp != self.tail):
                pre = temp 
                temp = temp.next 
            pre.next = None 
            self.tail = pre 
            self.length = self.length - 1 
        else: #ANy position 
            counter = 0 
            temp = self.head 
            pre = self.head 
            while counter < index: 
                pre = temp 
                temp = temp.next
            pre.next = temp.next 
            self.length = self.length - 1

        
        


        


ll1 = LinkedList(2)

ll1.append_end(3)
ll1.append_end(7)
ll1.append_end(12)
ll1.append_end(24)
ll1.append_end(42)
ll1.append_end(77)

ll1.append_first(1)
ll1.append_first(0)

ll1.pop_end()
ll1.pop_end()

ll1.pop_first()

ll1.get_val(0)
ll1.get_val(3)

ll1.replace_val(100, 0)
ll1.replace_val(400, 3)
ll1.replace_val(300, 2)
ll1.replace_val(200, 1)

ll1.append_first(15)

ll1.remove_any(0)
ll1.remove_any(1)

ll1.print()
print(ll1.tail.value)