'''
- Code Design:
  + Initializes two variables, min_val and max_val, with the first element of the list. This initialization allows for comparison with all other elements in the list.
  + The core of the function is a single loop that iterates through each element of the list once.
  +  During each iteration, the function compares the current element with the existing min_val and max_val and updates them.

- Efficiency:
  + Time complexity: O(n). It goes through the list only once.

'''

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # Check for an empty list
    if len(ints) == 0:
        return (None, None)

    min_val = max_val = ints[0]

    # Single traversal to find both min and max
    for num in ints:
        # Update min_val if a smaller number
        if num < min_val:
            min_val = num
        # Update max_val if a larger number
        elif num > max_val:
            max_val = num

    return (min_val, max_val)

# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
