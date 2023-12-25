'''
- Code Design:
  + The algorithm maintains three pointers low, mid, and high to partition the array into three sections.
  + The array is traversed only once.
  + The elements are swapped in place.

- Efficiency:
  + Time complexity:  O(n). Each element in the array is swapped at most once

'''

def sort_012(input_list):
    """
    Given an input array consisting only of 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low = 0
    high = len(input_list) - 1
    mid = 0

    # Traverse the list only once
    while mid <= high:
        if input_list[mid] == 0:
            # Swap if the element is 0, move both low and mid pointers
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        # Move mid pointer if element is 1
        elif input_list[mid] == 1:
            mid += 1
        # input_list[mid] == 2
        else:
            # Swap if the element is 2, move only the high pointer
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
