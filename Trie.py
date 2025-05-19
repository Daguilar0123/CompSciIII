#trie_autocorrect.py

class TrieNode:
    """
    A single node in the Trie-just like a ListNode in our LinkedList
    exercises.
    """
    # constructor
    def __init__(self):
        # children is a dict mapping character → TrieNode,
        # analogous to a 'next' pointer (or multiple 'next's) in ListNode.
        self.children = {}
        # is_end flags the end of a valid word, similar to marking the top
        # of a stick.
        self.is_end = False

class Trie:
    """
    Trie with insert/search and 
    """
    # constructor
    def __init__(self):
        # root is like the head of a linked list or the root of a BST.
        self.root = TrieNode()
        
    def insert(self, word):
        """
        Insert a word: similar to push() in SimpleStack,
        but we traverse/extend the path character by character.
        """
        node = self.root
        for ch in word:
            # If this character-path doesn't exist, create a new node:
            # like allocating a new ListNode when building a linked list.
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        #Mark the end-just like setting a flag at the top of the stack.
        node.is_end = True

    def search(self, word):
        """
        Exact-word lookup: like BST search, we walk down _find_node.
        Returns True only if we end on a node marked is_end.
        """
        node = self._find_node(word)
        return node is not None and node.is_end
    
    def starts_with(self, prefix):
        """
        Prefix check: reuses the same traversal as search(),
        similar to how we shared code between pop() and peek().
        """
        return self._find_node(prefix) is not None
    
    def _find_node(self, s):
        """
        Helper to walk s character-by-character, like stepping through a stack
        or list.
        Returns the final node or None if any step fails.
        """
        node = self.root
        for ch in s:
            if ch in node.children:
                node = node.children[ch]
            else:
                return None
        return node
    
    def all_words(self):
        """
        Collect every word via DFS-just like our graph DFS using a stack.
        Returns a Python list of strings."""
        results = []
        self._collect_all(self.root, "", results)
        return results
    
    def _collect_all(self, node, path, results):
        """
        Recursive tree traversal (like in the BST from class):
        if node.is_end, record the path; then recurse on each child.
        """
        if node.is_end:
            results.append(path)
        for ch in node.children:
            self._collect_all(node.children[ch], path + ch, results)