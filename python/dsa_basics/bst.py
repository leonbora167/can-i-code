class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_value(self, value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
            return True 
        
        temp = self.root
        while True:
            if new_node.value == temp.value:
                print("Value already exists")
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node 
                    return True 
                temp = temp.left 
            else:
                if temp.right is None:
                    temp.right = new_node 
                    return True 
                temp = temp.right 

    def contains(self, value):
        temp = self.root 
        while temp is not None:
            if value < temp.value:
                temp = temp.left 
            elif value > temp.value:
                temp = temp.right 
            else:
                print("Value exists")
                return True 
        print("Value does not exist")
        return False
    
    def _r_contains(self, current_node, value): #Checking recursively 
        if current_node == None:
            print("Tree empty")
            return False 
        if value == current_node.value:
            print("Value Found")
            return True #Base case to stop the recursion calls 
        if value < current_node.value:
            return self._r_contains(current_node.left, value)
        if value > current_node.value:
            return self._r_contains(current_node.right, value)
    def recursive_contains(self, value):
        return self._r_contains(self.root, value)
    
    def _r_insert(self, current_node, value):
        if current_node == None:
            print("Value Inserted")
            return Node(value)
        if value < current_node.value:
            current_node.left = self._r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self._r_insert(current_node.right, value)

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return True 
        self._r_insert(self.root, value)
    

my_tree = BinarySearchTree()
my_tree.insert_value(45)
my_tree.insert_value(32)
my_tree.insert_value(60)

print(my_tree.root.value) 
print(my_tree.root.left.value)
print(my_tree.root.right.value)

my_tree.contains(60)
my_tree.contains(37)

my_tree.recursive_contains(60)
my_tree.recursive_contains(37)

my_tree.r_insert(21)