# Class Node defination
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

# Insertion
def insert_element(root,k):
    if root is None:
        return Node(k)
        
    if k < root.data:
        root.left = insert_element(root.left, k)
    elif k > root.data:
        root.right = insert_element(root.right, k)
    
    return root
    
# Initializing a BST
root = Node(10)
insert_element(root, 5)

nodes = [5, 18, 8, 3, 15, 25, 17]

for i in nodes:
    insert_element(root, i)

# Searching a element 
def search_element(root, k):
    if root.data == k:
        return root
    
    if k < root.data:
        return search_element(root.left, k)
    elif k > root.data:
        return search_element(root.right, k)

#print(search_element(root, 15).right.data)

# Finding Min value
def findmin(root):
    current_node = root
    while current_node.left is not None:
        print(current_node.data)
        current_node = current_node.left
    return current_node

# Finding max value
def findmax(root):
    current_node = root
    while current_node.right is not None:
        print(current_node.data)
        current_node = current_node.right
    return current_node

#print(findmax(root))



# Deleting a element
def delete_element(root, k):
    if root is None:
        return root
    
    if k < root.data:
        root.left = delete_element(root.left, k)
    elif k > root.data:
        root.right = delete_element(root.right, k)
    else:
        # No child or one child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Both child
        temp = findmin(root.right)
        root.data = temp.data
        root.right = delete_element(root.right, temp.data)

    return root

        
# transvers (inorder)
def inorder_transvers(root):
    if root:
        inorder_transvers(root.left)
        print(root.data, end=" ")
        inorder_transvers(root.right)

def preorder_transvers(root):
    if root:
        print(root.data, end=" ")
        preorder_transvers(root.left)
        preorder_transvers(root.right)

def postorder_transvers(root):
    if root:
        postorder_transvers(root.left)
        postorder_transvers(root.right)
        print(root.data, end=" ")


inorder_transvers(root)
print()
preorder_transvers(root)
print()
postorder_transvers(root)
    



