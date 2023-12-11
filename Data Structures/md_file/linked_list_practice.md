# Tables of Contents
- ### [Implement a Linked List](#Implement-a-linked-list)


## Implement a linked list
```Python
# A node have two attributes: data and next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a node to the end of the list."""
        # Create a new node from the data
        new_node = Node(data)
        # Check the list is empty or not, if empty, add to the head
        if self.head is None:
            self.head = new_node
            return

        # If list not None, find the tail
        last_node = self.head
        # While till reach the tail, tail have node.next is None
        while last_node.next:
            last_node = last_node.next
        # Add new node to the tail of the list
        last_node.next = new_node

    def remove(self, data):
        """Remove the first node with the desired data."""
        # If list is empty, return
        if self.head is None:
            return
        # if the head needs to remove, remove the head node
        if self.head.data == data:
            self.head = self.head.next
            return

        # If node, traverse from the head to find the node needs to remove
        cur_node = self.head
        prev_node = None
        while cur_node and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next

        # if the data is not present
        if not cur_node:
            return

        # remove the node
        prev.next = cur_node.next
        cur_node = None

    def pop(self):
        """Remove the last element of the list and return the data."""
        # if list is empty, return
        if self.head is None:
            return

        # if the list has only one element
        if self.head.next is None:
            self.head = None

        # Traverse to the second-to-last node
        cur_node = self.head
        prev_node = None
        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next

        # Remove the last node
        prev_node.next = None

        return cur_node.data
```
