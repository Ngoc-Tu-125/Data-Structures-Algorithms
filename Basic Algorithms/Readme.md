# Basic Algorithms


## Binary Search
### Summary:
- Binary search is a search algorithm where we find the position of a target value by comparing the middle value with this target value.
- If the middle value is equal to the target value, then we have our solution(We have found the position of our target value).
- If the target value comes before the middle value, we look for the target value in the left half.
- Otherwise, we look for the target value in the right half.
- We repeat this process as many times as needed. until we find the target value.

### Code examples
```Python
def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        # Find the mid index
        mid_index = (start_index + end_index)//2
        # Get the element in this mid index
        mid_element = array[mid_index]

        # Compare mid element with target
        if target == mid_element:
            return mid_index
        elif target > mid_element:
            # If target > mid_element, continue with the right
            start_index = mid_index + 1
        else:
            # Else continue with the left
            end_index = mid_index

    return -1

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index_target = 6
answer = binary_search(array, target)
assert answer == index_target

```
Or using recursion
```Python
def binary_search_recursive(array, target):
    '''
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    mid_index = (start_index + end_index)//2

    mid_element = array[mid_index]

    if target == mid_element:
        return mid_index
    elif target > mid_element:
        return binary_search_recursive_soln(array, target, mid_index+1, end_index)
    else:
        return binary_search_recursive_soln(array, target, start_index, mid_index)

    return -1
```