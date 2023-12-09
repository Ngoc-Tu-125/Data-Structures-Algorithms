class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        # Init a head and tail node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # Init a linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        # Set the new node to the right after head
        node.prev = self.head
        node.next = self.head.next
        # Link new node the current head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        # Remove an existing node from the linked list.
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        # Move certain node in between to the head.
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        # Pop the current tail.
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key):
        node = self.cache.get(key, None)
        # Cache miss
        if not node:
            return -1
        # Move the accessed node to the head
        self._move_to_head(node)
        return node.value

    def set(self, key, value):
        node = self.cache.get(key)
        # If node is not exist in the cache now
        if not node:
            # Create a new Node
            newNode = Node(key, value)
            # Add to the cache
            self.cache[key] = newNode
            # Add to the linked list
            self._add_node(newNode)
            # If the cache over
            if len(self.cache) > self.capacity:
                # Pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            # Update the value.
            node.value = value
            self._move_to_head(node)

# Example Usage
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached its capacity and 3 was the least recently used entry

# Test case 1
def test_case_1():
    # Test set and get in normal
    cache_test = LRU_Cache(2)
    cache_test.set(1, 1)
    cache_test.set(2, 2)
    assert cache_test.get(1) == 1
    assert cache_test.get(2) == 2

# Test case 2
def test_case_2():
    # Test get and set with over capacity
    cache_test = LRU_Cache(2)
    cache_test.set(1, 1)
    cache_test.set(2, 2)
    assert cache_test.get(1) == 1
    cache_test.set(3, 3)
    assert cache_test.get(2) == -1

# Test case 3
def test_case_3():
    # Test with set exist key
    cache_test = LRU_Cache(2)
    cache_test.set(1, 1)
    cache_test.set(2, 2)
    assert cache_test.get(1) == 1
    assert cache_test.get(2) == 2
    cache_test.set(2, 5)
    assert cache_test.get(2) == 5
