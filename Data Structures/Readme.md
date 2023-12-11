# Data Structures
## List and Linked List
### List
List is a commonly used data structure. List might be of different types.
You can see the properties of lists like:
- Have an **order** (You can get the item by using the index)
- Have **no fixed length** (You can add or remove elements)

Some code example about List in python:
```python
>>> my_list = ['a', 'b', 'c']
>>> my_list[0]
'a'
>>> my_list[1]
'b'
```

### Linked List
A linked list is a fundamental data structure in computer science, commonly used in various programming langues. \
A linked list is a sequential collection of elements, but unlike array, the elements are not stored in contiguous memory locations.Instead, each element contains the data and a reference(or a link) to the next node in the sequence. \
**Node Structure in Linked List** \
A node in the linked list will have two attributes:
- **data**: The actual data that the node stores
- **next**: A reference(or a pointer) to the next node in the list

**Types of Linked List**
- **Singly Linked List**: Each node has only one link pointing to the next node.
- **Doubly Linked List**: Each node has two links, one to the next node and another to the previous node.
- **Circular Linked List**: The last node points to the first node, making a circle.

Now, let's implement a simple Linked List in python:
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
        """This function append the new node to the tail of the list."""
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

```

## [Linked List Practice](./md_file/linked_list_practice.md)