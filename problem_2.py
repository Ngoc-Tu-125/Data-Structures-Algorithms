import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # If path is not a directory return None
    if not os.path.isdir(path):
        return None

    # if suffix is empty return None
    if suffix == '':
        return None

    # create an empty list store all of the path found
    list_path = []

    # for each item in the directory at path
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        # if item path is a directory
        if os.path.isdir(item_path):
            # recursively call find_files with this directory
            # add results to list path
            list_path.extend(find_files(suffix, item_path))
            # else if item is a file and ends with suffix
        elif os.path.isfile(item_path) and item_path.endswith(suffix):
            # add the path to list path
            list_path.append(item_path)

    # return list path
    return list_path

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values


CUR_DIR = os.getcwd()
TEST_DIR = os.path.join(CUR_DIR, 'testdir')
## Test Case 1
def test_case_1():
    # Find files with test dir
    list_path = find_files('.c', TEST_DIR)
    assert list_path is not None

    sub_dir1 = os.path.join(TEST_DIR, 'subdir1')
    list_path = find_files('.c', sub_dir1)
    assert list_path[0] == os.path.join(sub_dir1, 'a.c')

## Test Case 2
def test_case_2():
    # Find files with test dir is not a directory
    test_file = sub_dir1 = os.path.join(TEST_DIR, 'subdir1', 'a.c')

    list_path = find_files('.c', test_file)

    assert list_path is None

## Test Case 3
def test_case_3():
    # Find files with suffix is empty
    list_path = find_files('', TEST_DIR)

    assert list_path is None