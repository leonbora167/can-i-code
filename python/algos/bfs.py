#Bfs we travel level wise
# like all the vertices of one node has to be explored before travelling to the next
# Simply can use queue structure where its FIFO

#Assuming the tree is a linked list

from collections import deque

def bfs(root):
    if not root:
        return None 
    
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        print(node.val)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result 

#What if I want to print level by level 

def bfs(root):
    if not root:
        return [] 
    queue = deque([root])

    while queue:
        level_len = len(queue)
        for i in range(level_len):
            node = queue.popleft() 
            print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        print()