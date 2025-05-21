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

    def edit_distance(self, a, b):
        """
        Levenshtein distance via a 2D DP table - (matrix of size (m+1)x(n+1)).
        """
        m = len(a)
        n = len(b)
        # initialize dp table
        dp = []
        for i in range(m+1):
            dp.append([0] * (n+1))
        # boundary conditions (first row/column )
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        # fill table-nested loops - dynamic programming
        for i in range(1, m+1):
            for j in range(1, n+1):
                if a[i-1] == b[j-1]:
                    cost = 0
                else:
                    cost = 1
                dp[i][j] = min(
                    dp[i-1][j] +1,          # deletion
                    dp[i][j-1] +1,          # insertion
                    dp[i-1][j-1] + cost     # substitution
                )
        return dp[m][n]
    
    def autocorrect(self, word, max_suggestions, max_distance):
        """
        Naïve autocorrect: for each stored word (from all_words),
        compute edit_distance and collect those within max_distance.
        Similar to sorting query results.
        """
        candidates = []
        for w in self.all_words():
            d = self.edit_distance(word, w)
            if d <= max_distance:
                candidates.append((d, w))
        # sort by (distance, word)
        candidates.sort()
        results = []
        count = 0
        for d, w in candidates:
            if count >= max_suggestions:
                break
            results.append(w)
            count += 1
        return results
    
def main():
    # 1) Build the trie—mirror SimpleStackClient.py
    words = ["to", "tea","teal", "ten", "in", "inn", "cat", "cot", "cut", "dog", "dot"]
    t = Trie()
    for w in words:
        t.insert(w)

    # 2) Test inputs—same for-loop style as DelimiterChecker or StackClient from book.
    tests = ["te", "teaa", "teh", "inn", "dug", "dt"]
    for w in tests:
        exact = t.search(w)
        if exact:
            suggestions = []
        else:
            suggestions = t.autocorrect(w, 3, 1)

        print("input:", w)
        print(" exact match?", exact)

        if not exact:
            print(" autocorrect suggestions:")
            for cand in suggestions:
                d = t.edit_distance(w, cand)
                # classify single‐edit operations
                if d == 1:
                    if len(cand) > len(w):
                        op = "insertion"
                    elif len(cand) < len(w):
                        op = "deletion"
                    else:
                        op = "substitution"
                else:
                    op = f"{d} edits"
                print(f"  - {cand!r}: # of single-character edits (distance) = {d}, operation = {op}")
        else:
            print(" autocorrect -> <skipped, exact match>")

        print("-" * 40)

if __name__ == "__main__":
    main()