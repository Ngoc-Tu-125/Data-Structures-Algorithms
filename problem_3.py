import sys
import heapq


# Node class for the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char  # Character
        self.freq = freq  # Frequency of the character
        self.left = None  # Left child
        self.right = None  # Right child

    # Comparison method for priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(data):
    # Function to build the Huffman Tree
    if not data:
        return None

    # Count the frequency of each character in the input data
    frequency = {}
    for char in data:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1

    # Create a priority queue (min-heap) of nodes based on frequencies
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    # Build the Huffman tree by merging two lowest frequency nodes at a time
    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)  # Node with lowest frequency
        right_node = heapq.heappop(priority_queue)  # Node with second lowest frequency
        merged_node = Node(None, left_node.freq + right_node.freq)  # Merge the two nodes
        merged_node.left = left_node
        merged_node.right = right_node
        # push merged_node back to piority_queue
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]  # Root of the Huffman tree


def generate_codes(node, prefix="", codebook={}):
    # Recursive function to generate Huffman codes for each character
    if node is None:
        return

    # If a leaf node is reached, add the code to the codebook
    if node.char is not None:
        codebook[node.char] = prefix

    # Recursively generate codes for left and right children
    generate_codes(node.left, prefix + "0", codebook)
    generate_codes(node.right, prefix + "1", codebook)

    return codebook


# Function for Huffman encoding
def huffman_encoding(data):
    root = build_huffman_tree(data)  # Build Huffman tree
    huffman_codes = generate_codes(root)  # Generate Huffman codes
    encoded_data = ''.join([huffman_codes[char] for char in data])  # Encode the data
    return encoded_data, root


# Function for Huffman decoding
def huffman_decoding(encoded_data, tree):
    decoded_output = ""
    current_node = tree
    for bit in encoded_data:
        # Traverse the Huffman tree based on the current bit
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        # If a leaf node is reached, append the character to the decoded output
        if current_node.left is None and current_node.right is None:
            decoded_output += current_node.char
            current_node = tree  # Return to the root of the tree

    return decoded_output


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
def test_case_1():
    # Test with data is normal case
    data = "The test case 1"

    encoded_data, tree = huffman_encoding(data)

    decoded_data = huffman_decoding(encoded_data, tree)

    assert decoded_data == data

## Test Case 2
def test_case_2():
    # Test with data is empty
    data = ""

    encoded_data, tree = huffman_encoding(data)

    decoded_data = huffman_decoding(encoded_data, tree)

    assert decoded_data == data

## Test Case 3
def test_case_3():
    # Test with data is very large values
    data = "Hello" * 1000

    encoded_data, tree = huffman_encoding(data)

    decoded_data = huffman_decoding(encoded_data, tree)

    assert decoded_data == data
