import math

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

    def k_from_end(self, k):
        first = self.head 
        second = self.head
        for i in range(k):
            first = first.next 

        while(first is not None):
            first = first.next 
            second = second.next 

        print("K element from end is : ", second.value)

    def remove_duplicates(self):
        var1 = self.head 
        var2 = self.head
        while(var1 != None):
            var2 = var1 
            while(var2.next != None):
                if(var2.next.value == var1.value):
                    var2.next = var2.next.next
                    self.length = self.length - 1
                var2 = var2.next 
            var1 = var1.next

    def binary_conversion(self):
        p = self.head
        length = 0
        while(p is not None):
            p = p.next 
            length += 1 
        factor = length - 1
        p = self.head 
        cal = []
        while(p is not None):
            temp = p.value * math.pow(2, factor)
            factor = factor - 1
            cal.append(temp)
            p = p.next 
        s = 0
        for i in cal:
            s += i 
        print("Summation is ",s)

    def partition_list(self, n):
        less_head = Node(0)
        greater_head = Node(1)
        less_tail = less_head
        greater_tail = greater_head

        current = self.head 
        while(current is not None):
            if(current.value < n):
                less_tail.next = current 
                less_tail = less_tail.next
            else:
                greater_tail.next = current 
                greater_tail = greater_tail.next 
            current = current.next

        less_head = less_head.next 
        greater_head = greater_head.next 
        greater_tail.next = None 
        less_tail.next = greater_head
        self.head = less_head

    def reverse_between(self, left, right):
        if(left == right or self.head is None):
            return self.head 
        dummy = Node(0)
        dummy.next = self.head 
        prev = dummy
        for i in range(left-1):
            prev = prev.next 
        
        curr = prev.next 
        k = right - left + 1
        tail = curr

        prev_sub = None 
        for i in range(k): #Reverse for k iterations
            nxt = curr.next 
            curr.next = prev_sub
            prev_sub = curr 
            curr = nxt 
        prev.next = prev_sub
        tail.next = curr 

    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head 
        
        prev = dummy 
        while(prev.next is not None and prev.next.next is not None):
            first = prev.next
            second = first.next

            #Simple swapping
            first.next = second.next
            second.next = first
            prev.next = second 

            prev = first 

        self.head = dummy.next 
        #Update tail
        temp = self.head 
        while(temp.next is not None):
            temp = temp.next
        self.tail = temp

        

        

        



ll1 = LinkedList(2)

ll1.append_start(3)
ll1.append_start(22)
ll1.append_start(33)
ll1.append_start(54)
ll1.append_start(1)
ll1.append_start(3)
ll1.append_start(100)

ll1.print()

ll1.find_middle()

ll1.k_from_end(3)

ll1.remove_duplicates()
ll1.print()

ll1.binary_conversion()

ll1.partition_list(30)
ll1.print()

ll1.swap_pairs()
ll1.print()