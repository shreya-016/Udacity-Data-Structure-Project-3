# Request routing in a web server using tries
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode()
        self.root.handler = handler
        
    def insert(self, path, handler):
        curr = self.root
        for route in path:
            if route not in curr.children:
                curr.insert(route)
            curr = curr.children[route]
        curr.handler = handler
        curr.isLeaf = True
            
                
    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr = self.root        
        for route in path:
            if route not in curr.children:
                return None
            curr = curr.children[route]
        if curr.isLeaf:
            return curr.handler
        else:
            return None
            

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None
        self.isLeaf = False

    def insert(self, path):
        self.children[path] = RouteTrieNode()
        
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler)
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(path)
        self.router.insert(path, handler)
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path = self.split_path(path)
        if path is None:
            code = 400
            handler = self.router.root.handler
            return code, handler
        handler = self.router.find(path)
        if handler is not None:
            code = 400
            return code, handler
        
        code = 404
        handler = "not found handler"
        return code, handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path.startswith('/'):
            path = path[1:]
        if path.endswith('/'):
            path = path[:-1]
        if len(path) == 0:
            return None
        return path.split('/')
        
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router = Router("root handler")
router.add_handler("/home/about", "about handler")
router.add_handler("/home/about/team/", "team handler")
router.add_handler("/app/images/2022/flowers", "flower handler")

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/team")) # should print 'team handler' 
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/app/images/2022/flower")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/app/images/2022/flowers")) # should print "flower handler"
