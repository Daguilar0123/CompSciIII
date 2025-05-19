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
    def __init__(self, word):
        # root is like the head of a linked list or the root of a BST.
        self.root = TrieNode()
        
        """
        Insert a word: similar to push() in SimpleStack,
        but we traverse/extend the path character by character.
        """
        