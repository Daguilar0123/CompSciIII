"""
Problem 6.4:
Write a program that solves the knapsack problem for an arbitrary
knapsack capacity and series of weights. Assume the weights are stored
in a list. The recursive knapsack() function's arguments are:

    - target: the remaining weight to fill
    - weights: the list of available item weights
    - index: the current index into weights
    - current: a LinkedList of the items selected so far

The function should print each combination of weights that sums exactly
to the original target.
"""

class Link:
    # One datum in a linked list
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setNext(self, link):
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception("Next link must be Link or None")

    def __str__(self):
        return str(self.getData())


class LinkedList:
    # Minimal singly linked list
    def __init__(self):
        self.__first = None

    def getFirst(self):
        return self.__first

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
        else:
            raise Exception("First link must be Link or None")

    def isEmpty(self):
        return self.getFirst() is None

    def insert(self, datum):
        # Insert new datum at front of list
        new_link = Link(datum, self.getFirst())
        self.setFirst(new_link)

    def __iter__(self):
        # Allow iteration: for d in linked_list
        link = self.getFirst()
        while link is not None:
            yield link.getData()
            link = link.getNext()

    def __str__(self):
        pieces = [str(d) for d in self]
        return "[" + " > ".join(pieces) + "]"


def knapsack(target, weights, index=0, current=None):
    """
    Recursive knapsack() per Problem 6.4:

    - Base cases:
        * target == 0               → print current list (found a solution)
        * index >= len(weights)     → no more items, stop
        * target < 0                → overshot, stop

    - Recursive steps:
        1) Include weights[index]:
            • copy current into new_list
            • new_list.insert(weights[index])
            • recurse with (target - weights[index], index+1, new_list)
        2) Exclude weights[index]:
            • recurse with (target, index+1, current)
    """
    # ---- Initialize current list ----
    if current is None:
        current = LinkedList()

    # ---- Base cases ----
    if target == 0:
        print(current)
        return
    if index >= len(weights) or target < 0:
        return

    # ---- Include current weight ----
    # Copy current into a new list so we don't mutate it
    new_list = LinkedList()
    for d in reversed(list(current)):  # preserve order
        new_list.insert(d)
    new_list.insert(weights[index])
    knapsack(target - weights[index], weights, index + 1, new_list)

    # ---- Exclude current weight ----
    knapsack(target, weights, index + 1, current)


# ---------------- Demo / Output ----------------
if __name__ == "__main__":
    W = [11, 8, 7, 6, 5]
    T = 20
    print(f"Knapsack combinations for target = {T} and weights = {W}:")
    knapsack(T, W)