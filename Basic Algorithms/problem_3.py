'''
- Code Design:
  + Uses a custom merge sort to sort the array in descending order, ensuring an O(nlog(n)) time complexity.
  + It alternately picks digits from the sorted array to form two numbers.
  + The function ensures that the two formed numbers have the maximum possible sum and that their digit counts do not differ by more than 1.
  + Merge Sort:
    * The merge_sort function is customized to sort the array in descending order. This sorting ensures that the highest digits are placed first when forming the numbers,
    maximizing their sum.
    * Merge sort employs a divide-and-conquer strategy, dividing the array into halves, sorting them independently, and then merging them.
  + Once the array is sorted in descending order, the rearrange_digits function alternates between picking digits for forming two numbers.
  + By sorting the array in descending order and alternately picking digits, the function maximizes the sum of the two numbers formed.

- Efficiency:
  + Time complexity: O(nlog(n)) due to merge sort.
  This is because the array is divided into halves (log(n) divisions) and each of these divisions requires a linear time merge operation (n).
  + Space complexity: O(n) primarily due to the recursive nature of merge sort. In each recursive call, new arrays (left_half and right_half) are created,
  which collectively can take up to n space in total

'''
def merge_sort(array):
        """
        Sorts an array in descending order using merge sort.

        Args:
           array(list): The array to sort
        Returns:
           list: Sorted array in descending order
        """
        # Single element array is already sorted
        if len(array) > 1:
            # Divide the array into two halves
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            # Recursive calls to sort both halves
            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0

            # Merging left and right halves
            while i < len(left_half) and j < len(right_half):
                if left_half[i] > right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            # Copy remaining elements of left_half
            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            # Copy remaining elements of right_half
            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two numbers such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Sort the array in descending order
    merge_sort(input_list)

    # Build the two numbers from the sorted array
    number1, number2 = 0, 0
    for i, num in enumerate(input_list):
        # If index is even, append to number1
        if i % 2 == 0:
            number1 = number1 * 10 + num
        # If index is odd, append to number2
        else:
            number2 = number2 * 10 + num

    return [number1, number2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Test with larger numbers will failed because the range of function is [0,9] => Failed
test_function([[10, 20, 30, 40, 50], [5040, 310]])
# Test with an empty array
test_function([[], [0, 0]])
# Test with All Same Digits
test_function([[7, 7, 7, 7], [77, 77]])

