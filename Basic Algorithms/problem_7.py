'''
- Code Design:
  + RouteTrieNode: Each node represents a part of the path, storing its children and an optional handler.
 Handlers are associated only with the nodes representing the end of complete paths.
  + RouteTrie: This Trie structure is specifically designed for routing paths. It includes methods to insert new paths with their handlers and to find a handler for a given path.
  + Router: This class wraps around RouteTrie, providing an interface to add handlers for specific paths and to look up handlers based on a given URL path.

- Efficiency:
  + Time complexity:
    Insert: O(n).  n is the number of parts in the path.
    Lookup: O(n).  n is the number of parts in the path.

'''

## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        """Initialize the trie with an root node and a handler, this is the root path or home page node."""
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_parts, handler):
        '''
        Similar to our previous example you will want to recursively add nodes
        Make sure you assign the handler to only the leaf (deepest) node of this path
        '''
        current_node = self.root
        for part in path_parts:
            # Traverse down the Trie, creating nodes as needed
            current_node.insert(part)
            current_node = current_node.children[part]
        # Assign the handler to the leaf node of this path
        current_node.handler = handler

    def find(self, path_parts):
        '''
        Starting at the root, navigate the Trie to find a match for this path
        Return the handler for a match, or None for no match
        '''
        current_node = self.root
        for part in path_parts:
            # Traverse down the Trie
            if part in current_node.children:
                current_node = current_node.children[part]
            else:
                # Path part not found, return None
                return None
        # Return the handler for the found path
        return current_node.handler

## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        """Initialize the node with children as before, plus a handler."""
        self.children = {}
        self.handler = handler

    def insert(self, path_part, handler=None):
        '''Insert the node as before.'''
        if path_part not in self.children:
            # Create a new node if the path part is not already a child
            self.children[path_part] = RouteTrieNode(handler)

## The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        '''
        Create a new RouteTrie for holding our routes
        You could also add a handler for 404 page not found responses as well!
        '''
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        '''
        Add a handler for a path
        You will need to split the path and pass the pass parts
        as a list to the RouteTrie
        '''
        # Split the path into parts
        path_parts = self.split_path(path)
        # Insert the path and handler into the Trie
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        '''
        lookup path (by parts) and return the associated handler
        you can return None if it's not found or
        return the "not found" handler if you added one
        bonus points if a path works with and without a trailing slash
        e.g. /about and /about/ both return the /about handler
        '''
        # Split the path into parts
        path_parts = self.split_path(path)
        # Find the handler in the Trie
        handler = self.route_trie.find(path_parts)
        # Return the handler or not found handler
        return handler if handler else self.not_found_handler

    def split_path(self, path):
        '''
        you need to split the path into parts for
        both the add_handler and loopup functions,
        so it should be placed in a function here
        '''
        # Strip leading and trailing slashes and split the path
        return [part for part in path.strip('/').split('/') if part]

# Test cases
## create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

