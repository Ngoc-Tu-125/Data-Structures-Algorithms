import hashlib

def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash(data + timestamp + previous_hash)


class Blockchain:
    def __init__(self):
        # Initialize the blockchain with no blocks.
        self.tail = None

    def add_block(self, timestamp, data):
        # Function to add a new block to the blockchain.
        if self.tail is None:
            previous_hash = '0'
        else:
            previous_hash = self.tail.hash

        new_block = Block(timestamp, data, previous_hash)

        self.tail = new_block

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
def test_case_1():
    # Test with normal case with two block
    blockchain = Blockchain()
    blockchain.add_block("2023-12-09 10:00", "First Block")
    first_block_hash = blockchain.tail.hash
    blockchain.add_block("2023-12-09 10:05", "Second Block")
    assert blockchain.tail.previous_hash == first_block_hash

## Test Case 2
def test_case_2():
    # Test with normal case with one block
    blockchain = Blockchain()
    blockchain.add_block("2023-12-09 10:00", "First Block")
    assert blockchain.tail.previous_hash == '0'

## Test Case 3
def test_case_3():
    # Test with empty case
    blockchain = Blockchain()
    assert blockchain.tail is None