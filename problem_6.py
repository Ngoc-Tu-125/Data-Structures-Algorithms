class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Use a set to avoid duplicates
    union_set = set()
    current = llist_1.head

    # Traverse the first list
    while current:
        union_set.add(current.value)
        current = current.next

    # Traverse the second list
    current = llist_2.head
    while current:
        union_set.add(current.value)
        current = current.next

    # Convert the set back into a linked list
    union_list = LinkedList()
    for value in union_set:
        union_list.append(value)

    return union_list


def intersection(llist_1, llist_2):
    # Use a set to avoid duplicates
    set_1 = set()
    intersection_set = set()

    # Add all elements of the first list
    current = llist_1.head
    while current:
        set_1.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        # Check if elements of the second list are in set_1
        if current.value in set_1:
            # If yes, add to intersection_set
            intersection_set.add(current.value)
        current = current.next

    # Convert the intersection set to a linked list
    intersection_list = LinkedList()
    for value in intersection_set:
        intersection_list.append(value)

    return intersection_list


## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

def list_to_linked_list(lst):
    linked_list = LinkedList()
    for item in lst:
        linked_list.append(item)
    return linked_list


def linked_list_to_list(linked_list):
    result = []
    current = linked_list.head
    while current:
        result.append(current.value)
        current = current.next
    return result

## Test Case 1
def test_case_1():
    # Test with normal case
    ll1 = list_to_linked_list([1, 2, 3, 4])
    ll2 = list_to_linked_list([1, 2, 5, 6])

    expected_union = [1, 2, 3, 4, 5, 6]
    expected_intersection = [1, 2]

    assert sorted(linked_list_to_list(union(ll1, ll2))) == sorted(expected_union)
    assert sorted(linked_list_to_list(intersection(ll1, ll2))) == sorted(expected_intersection)

## Test Case 2
def test_case_2():
    # Test with a list is empty
    ll1 = list_to_linked_list([])
    ll2 = list_to_linked_list([1, 2, 3, 4])

    expected_union = [1, 2, 3, 4]
    expected_intersection = []

    assert sorted(linked_list_to_list(union(ll1, ll2))) == sorted(expected_union)
    assert linked_list_to_list(intersection(ll1, ll2)) == expected_intersection

## Test Case 3
def test_case_3():
    # Test with lager list size
    large_list_1 = list(range(1, 10001)) + [10000, 20000, 30000]  # Large list with extra elements
    large_list_2 = list(range(1000, 10000)) + [20000, 30000, 40000]  # Overlapping and distinct elements

    ll1 = list_to_linked_list(large_list_1)
    ll2 = list_to_linked_list(large_list_2)

    # Expected union and intersection results
    expected_union = list(set(large_list_1 + large_list_2))
    expected_intersection = list(set(large_list_1) & set(large_list_2))

    # Convert results from linked list to Python list and sort them for comparison
    assert sorted(linked_list_to_list(union(ll1, ll2))) == sorted(expected_union)
    assert sorted(linked_list_to_list(intersection(ll1, ll2))) == sorted(expected_intersection)