class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True

    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
def test_case_1():
    # Test with user in group
    assert is_user_in_group("sub_child_user", sub_child) == True

## Test Case 2
def test_case_2():
    # Test with Null user
    assert is_user_in_group(None, parent) == False

## Test Case 3
def test_case_3():
    # Test with nested group
    assert is_user_in_group("sub_child_user", parent) == True