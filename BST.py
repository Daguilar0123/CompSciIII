class Node:
    def __init__(self, key):
        # interpret key as data in node.
        self.key =key
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        # at a root or left.
        self.root=None
    def insert(self, key):
        def _insert(root, key):
            if root is None:
                return Node(key)
            if key<root.key:
                root.left=_insert(root.left,key)
            else:
                root.right=_insert(root.right,key)
            return root
        self.root=_insert(self.root,key)
    def print_tree(self):
        def _print_tree(node,level=0):
            if node is not None:
                _print_tree(node.right,level+1)
                print(" "*level+ f"->{node.key}")
                _print_tree(node.left,level+1)
            _print_tree(self.root)

            # helper function to facilitate tree traversals
            # The outside function is a public interface for the helper function
            # outside (public) function
            def pre_order(self): # root left right for printing a copy
                # helper (private) function
                def _preorder(node):
                    if node:
                        print(node.key,end="")
                        _preorder(node.left)
                        _preorder(node.right)
                _preorder(self.root)
                print()

            def in_order(self): # left node right good for sorted order
                def _inorder(node):
                    if node:
                        _inorder(node.left)
                        print(node.key,end="")
                        _inorder(node.right)
                _inorder(self.root)
                print()

            def post_order(self):   # left right root god for deleting trees
                def _post_order(node):
                    if node:
                        _post_order(node.left)
                        _post_order(node.right)
                        print(node.key,end="")
                _post_order(self.root)
                print()
            def search(self,target):
                def _search(node,target):
                    if node is None:
                        return None
                    if node.key == target:
                        return node
                    elif target<node.key:
                        return _search(node.left,target)
                    else:
                        return _search(node.right,target)
                return _search(self.root,target)

def main():
    bst = BST()
    for value in [50,30,70,20,40,60,80]:
        bst.insert(value)
    bst.print_tree()

if __name__=="__main__":
    main()