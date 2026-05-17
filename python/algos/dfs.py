#We try to start with one node and reach one node till the end - then travel back to the previous node - then travel to another node not travelled till now
# Keep track using stacks or recursion

def dfs(root):
    if not root:
        return 
    
    print(root.val) #The value explored by the graph 
    dfs(root.left)
    dfs(root.right)


#DFS pattern 

def dfs(node):
    if not node:
        return "<BASE_CASE>"
    
    left = dfs(node.left)
    right = dfs(node.right)

    #compute something using left + right 
    return "Result for THIS NODE"
    

#Height of subtree 
# Height = max depth from node ; depth - number of edges from node to root

def height(node):
    if not node:
        return 0
    left = height(node.left)
    right = height(node.right)
    return 1 + max(left, right)

# Size of subtree - number of nodes in the subtree 
def count(node):
    if not node:
        return 0 
    left = count(node.left)
    right = count(node.right)
    return 1 + left + right

#Diameter - longest length or number of vertexes between any two nodes 
def diameterofbt(root):
    diameter = 0
    def dfs(node):
        if not node:
            return 0 
        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left+right)
        return 1 + max(left, right)
    dfs(root)
    return diameter

#Height of every subtree 
res = {}
def height(root):
    if not root:
        return 0
    left = height(root.left)
    right = height(root.right)
    h = 1 + max(left, right)
    res[root.val] = h
    print(f"For Node : {root.val} Height : {h}")
    return h

#Size/Count of every subtree
def count(root):
    if not root:
        return 0 
    left = count(root.left)
    right = count(root.right)
    c = 1 + left + right 
    print(f"For Node : {root.val} Size : {c}")
    return 

#Depth of any node
# Depth is number of edges from "root" node
# Depth be calculated top-down since its from the root to that particular node
res = {}
def compute_depth(node, depth):
    if not node:
        return 0 
    print(f"For Node : {node.val} Depth : {depth}")
    res[node.val] = depth
    compute_depth(node.left, depth+1)
    compute_depth(node.right, depth+1)

compute_depth(root, 0)