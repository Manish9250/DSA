class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def removeDuplicates(head):
    current_node = head
    while current_node.next:
        if current_node.data == current_node.next.data:
            current_node.next = current_node.next.next
        current_node = current_node.next

def add_at_last(head, data_node):
    if head is None:
        head = Node(data_node.data)
    current_node = head
    while current_node.next:
        current_node = current_node.next
    current_node.next = Node(data_node.data)
    return head


new_node = Node(10)
last_node = Node(5)
new_node = add_at_last(new_node, last_node)
print(new_node.data, new_node.next.data)
last_node = Node(6)
new_node = add_at_last(new_node, last_node)
print(new_node.data, new_node.next.data, new_node.next.next.data)
