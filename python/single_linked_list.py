class LinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next 
    
class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_beginning(self, data):
        node = LinkedListNode(data, self.head)
        self.head = node 

    def print(self):
        if(self.head is None):
            print("Empty Linked List")
            return 
        
        iterator = self.head 
        string = ''

        while iterator:
            string += str(iterator.data) + " -> "
            iterator = iterator.next 

        print(string)


    def insert_at_end(self, data):
        if self.head is None:
            self.head = LinkedListNode(data, None) #If LL is blank then we will create the new node and its .next will be None 
            return 

        iterator = self.head 
        while iterator.next:
            iterator = iterator.next 

        iterator.next = LinkedListNode(data, None) #Last new node will be created and connected to the last element of the current ll


    def insert_values(self, data_list):
        self.head=None #Head of new LL is None 
        for i in data_list:
            self.insert_at_end(i) 
    

    def get_length(self):
        count = 0
        iterator = self.head #The ll object.head contains information about the first node which contains information about the next node and so on
        while iterator: #not .next since then it will run one extra time till the value is none
            count = count + 1
            iterator = iterator.next 
        return count 

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next 
            return 
        
        count = 0 
        iterator = self.head 
        while iterator:
            if count == index - 1: #To remove the element at n position i want to be at n-1 position through count
                iterator.next = iterator.next.next #will skip the element at n position and go to position n+1
            iterator = iterator.next
            count = count + 1 #When the iterator contains "None" the count will be the length of the ll and at count n it will be at the index n of the ll 

    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return 
        
        count = 0
        iterator = self.head 
        while iterator:
            if count == index - 1:
                node = LinkedListNode(data, iterator.next)
                iterator.next = node 
                break

            count = count + 1
            iterator = iterator.next 



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(8)
    ll.insert_at_beginning(24)
    '''
    From what I understand from a layman's perspective, for every insert operation first for the object 
    we are adding the value in .data and making .next=None for the first go and then making the .head of the 
    whole object.head as the node itself which contains .data and .next(None).
    In the second go we again pass the value which goes inside .data and then use the previously initialized .head 
    and put it inside this latest objects .next, hence this .next points/contains the previous node now with its .data and .next.
    Then we make this object which conatains the latest value in the first "position" as the head and this process continues further.
    '''   
    ll.insert_at_end(99)
    ll.insert_values(["Batman", "Robin", "Joker", "Batgirl"])
    ll.remove_at(2)
    ll.insert_at(2, "Superman")
    print("Length is ", ll.get_length())
    ll.print()
