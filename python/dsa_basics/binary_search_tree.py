class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 

class Binary_Tree:
    def __init__(self):
        self.root = None 

    def insert(self, value):
        new_node = Node(value) 
        if self.root == None:
            self.root = new_node
            return True 
        temp = self.root 
        while True:
            if new_node.value == temp.value:
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
                print("Value is there")
                return True 
        print("Value not present")
        return False

tree = Binary_Tree()
tree.insert(10)
tree.insert(50)
tree.insert(8)

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)

tree.contains(4)
tree.contains(8)