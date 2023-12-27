'''
- Code Design:
  + Using binary search because the good time complexity of it.
  + First, The square root of a number is always less than or equal to the number itself. It's mean that the square [from 0 to number].
  + In each iteration of the loop, the algorithm calculates a mid-point (mid) of the current range.
  + If the square of the mid-point (squared) is equal to the input number, the algorithm returns mid as the square root.
  + If squared is less than number, it means the square root must be higher than mid, so the algorithm adjusts the lower bound of the range to mid + 1.
  + If squared is more than number, it indicates the square root is less than mid, leading to the adjustment of the upper bound to mid - 1.
  + For numbers 0 and 1, the square root is the number itself.

- Efficiency:
  + Time complexity: O(log(n)) due to binary search.
  This is because with each iteration of the while loop, the search interval is halved, following the principle of binary search.
  + Space complexity: O(1). The algorithm uses a fixed amount of space regardless of the input size. It only requires a few variables to store
  the bounds of the search (low and high), the midpoint (mid), and the squared value of the midpoint (squared)

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
