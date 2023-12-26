'''
- Code Design:
  + Using binary search because the good time complexity of it.
  + The function first determines which half of the array is sorted and then decides where to search for the target.
  + In each iteration, the algorithm calculates a mid-point (mid). This is the potential candidate for the target number.
  + If the elements at start to mid are sorted (input_list[start] <= input_list[mid]), the algorithm checks if the target is within this range.
  + If the elements at mid to end are sorted, a similar approach is followed for this half.

  + The function returns -1 for an empty array

- Efficiency:
  + Time complexity: O(log(n)) due to binary search.
  + The rotated_array_search function splits the search space in half during each iteration.

'''


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array.

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1

    start, end = 0, len(input_list) - 1

    while start <= end:
        # Calculate the middle position
        mid = (start + end) // 2

        # Directly return the index if the middle element is the target
        if input_list[mid] == number:
            return mid

        # Check if the left half is sorted
        if input_list[start] <= input_list[mid]:
            # Target in the left sorted half
            if input_list[start] <= number < input_list[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # Right half is sorted
        else:
            # Target in the right sorted half
            if input_list[mid] < number <= input_list[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1

# Function to perform linear search for testing
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

# Test function to compare linear search and rotated array search results
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Testing
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Non-existent Case
test_function([[6, 7, 8, 1, 2, 3, 4], 10])