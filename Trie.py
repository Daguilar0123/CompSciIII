#trie_autocorrect.py

class TrieNode:
    """
    A single node in the Trie-just like a ListNode in our LinkedList
    exercises.
    """
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