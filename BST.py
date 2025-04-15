class Node:
    def __init__(self, key, data):
        self.key =key
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self, key):
        def _insert(root, key):
            if root is None:
                return Node(key)
            if key<root.key:
                root.left=insert(root.left,key)
            else:
                root.right=_insert(root.right,key)
            return root
        self.root=_insert(self.root,key)

newNode = Node()