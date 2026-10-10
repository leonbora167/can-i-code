class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None 

class Double:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value): #Append in beginning
        new_node = Node(value)
        self.head.prev = new_node
        new_node.next = self.head 
        self.head = new_node
        self.length = self.length + 1

    def print(self):
        temp = self.head 
        while(temp is not None):
            print(temp.value)
            temp = temp.next

    def palindrome(self):
        length = self.length 
        forward = self.head
        backward = self.tail
        n1, n2 = [], []
        for i in range(length):
            temp = forward.value
            n1.append(temp)
            forward = forward.next
        for i in range(length):
            temp = backward.value
            n2.append(temp)
            backward = backward.prev
        if(n1 == n2):
            print("Palindrome")
        else:
            print("Not a palindrome")
    
    def reverse(self): #swap every nodes next and prev simply -> O(n)
        if self.head is None or self.head.next is None: #empty list 
            return "List Empty"
        current = self.head 
        while current is not None:
            current.next, current.prev = current.prev, current.next 
            current = current.prev #Since the prev was originally next 
        self.head, self.tail = self.tail, self.head 

    def reverse_between(self, m, n):
        print(f"Reversing between {m} and {n}")
        if m==n:
            return "Invalid"
        if m<1 or n<1 or m>n or n>self.length:
            return "Invalid"
        
        idx = 1 
        current = self.head 
        before = None 
        while idx<m:
            before = current 
            current = current.next 
            idx = idx + 1 
            #Now current will be at m node and before is at one node before m 
        start = current # m-th node 

        while idx<n:
            current = current.next 
            idx += 1 
        end = current # n-th node 
        after = end.next # node after n-th node 
        #now we have node before m-th node, m-th node, n-th node, node after n-th node 
        
        node = start 
        while True:
            node.next, node.prev = node.prev, node.next 
            if node is end:
                break 
            node = node.prev
        
        if before:
            before.next = end 
            end.prev = before 
        else:
            self.head = end 
            end.prev = None
        if after:
            start.next = after 
            after.prev = start
        else:
            self.tail = start 
            start.next = None  

    def swap_pairs(self):
        print("Swapping Pairs")
        if self.head is None or self.tail is None:
            return "Invalid"
        
        current = self.head 
        while current is not None and current.next is not None:
            first = current 
            second = current.next 
            before = first.prev     # when first is head, before -> None
            after = second.next     # When second is tail, after -> None 

            if before:
                before.next = second 
            else:
                self.head = second #Second is now the new head for this llv

            second.prev = before
            second.next = first 
            first.prev = second 
            first.next = after 
            
            if after:
                after.prev = first 
            else:
                self.tail = first 

            current = after 



        



dl = Double(1)
dl.append(1)
dl.append(1)
dl.append(3)
dl.append(4)
dl.append(8)
dl.print()

dl.palindrome()

dl.reverse()
dl.print()
dl.reverse_between(2, 5)
dl.print()
dl.swap_pairs()
dl.print()