'''
- Code Design:
  + Using binary search because the good time complexity of it.

- Efficiency:
  + Time complexity: O(log(n)) due to binary search

'''

def sqrt(number):
    """
    Calculate the floored square root of a number using binary search.

    Args:
       number(int): Number to find the floored square root
    Returns:
       int: Floored Square Root
    """

    # For numbers less than 2, return the number itself (0 or 1)
    if number < 2:
        return number

    low, high = 0, number

    # Binary search loop
    while low <= high:
        # Calculate the middle value
        mid = (low + high) // 2
        # Square the middle value
        squared = mid * mid

        # Check if the squared value is equal to the input number
        if squared == number:
            return mid
        # If squared is less than the input number, adjust the lower bound
        elif squared < number:
            low = mid + 1
        # If squared is more than the input number, adjust the upper bound
        else:
            high = mid - 1

    # Return the floor value of the square root
    return high

# Test cases
print("Pass" if (3 == sqrt(9)) else "Fail")  # Normal case
print("Pass" if (0 == sqrt(0)) else "Fail")  # Edge case: zero
print("Pass" if (4 == sqrt(16)) else "Fail") # Normal case
print("Pass" if (1 == sqrt(1)) else "Fail")  # Edge case: one
print("Pass" if (5 == sqrt(27)) else "Fail") # Non-perfect square
