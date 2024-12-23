class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)

    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_start(data)
            return
        else:
            current_node = self.head
            new_node = Node(data)
            for _ in range(position-1):
                if current_node.next:
                    current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            
    def delete_from_start(self):
        if self.head:
            self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def delete_by_value(self, data):
        if not self.head:
            return
        elif self.head.data == data:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next:
                if current_node.next.data == data:
                    current_node.next = current_node.next.next
                    return
                current_node = current_node.next

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False


    def transvers(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            if prev:
                print(f"Changing Current node [{current.data}] next to previous [{prev.data}]: ", )
            current.next = prev
            if prev:
                print(f"setting prev [{prev.data}] to current [{current.data}]")
            prev = current
            current = next_node
        self.head = prev


# Create a linked list
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)



ll.transvers()
print()

print(ll.reverse())

ll.transvers()
#print()
#ll.insert_at_position(1, 50)
#ll.transvers()