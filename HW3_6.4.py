"""
Problem 6.4: The Knapsack Problem

Write a program that solves the knapsack problem for an arbitrary
knapsack capacity and series of weights. Assume the weights are stored
in an array. The recursive knapsack() function’s arguments are:

  • target: the remaining weight to fill
  • weights: the list of item weights
  • index: the current position in the weights array
  • current: a LinkedList of the items selected so far

When the sum of selected items equals the original target, the function
prints the list of weights in the knapsack.
"""

# ----------------------------------------------------------------------
# Chapter 5 Linked-List Implementation
# ----------------------------------------------------------------------

class Link(object):  # One datum in a linked list
    def __init__(self, datum, next=None):          # Constructor Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        self.__data = datum
        self.__next = next

    def getData(self):                             # Return stored datum
        return self.__data

    def setData(self, datum):                      # Change stored datum
        self.__data = datum

    def getNext(self):                             # Return next Link
        return self.__next

    def setNext(self, link):                       # Change next Link Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception("Next link must be Link or None")

    def isLast(self):                              # Test if this is the last Link
        return self.getNext() is None

    def __str__(self):                             # String representation of Link
        return str(self.getData())


def identity(x): return x                        # Helper key function Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)


class LinkedList(object):  # A linked list of data elements

    def __init__(self):                             # Constructor Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        self.__first = None

    # Basic accessors and tests
    def getFirst(self): return self.__first         # Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
    def setFirst(self, link):                       # Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        if link is None or isinstance(link, Link):
            self.__first = link
        else:
            raise Exception("First link must be Link or None")

    def getNext(self): return self.getFirst()       # Synonym for getFirst Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
    def setNext(self, link): self.setFirst(link)    # Synonym for setFirst Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)

    def isEmpty(self):                              # Test for empty list Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        return self.getFirst() is None

    def first(self):                                # Return first item, not Link Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        if self.isEmpty():
            raise Exception("No first item in empty list")
        return self.getFirst().getData()

    # Traversal and utility methods
    def traverse(self, func=print):                  # Apply func to each item ‡Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        link = self.getFirst()
        while link is not None:
            func(link.getData())
            link = link.getNext()

    def __len__(self):                               # Enable len(self) ‡Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        l, link = 0, self.getFirst()
        while link is not None:
            l += 1
            link = link.getNext()
        return l

    def __str__(self):                               # String form: [a > b > …] ‡Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        result, link = "[", self.getFirst()
        while link is not None:
            if len(result) > 1: result += " > "
            result += str(link)
            link = link.getNext()
        return result + "]"

    # Insertion and search
    def insert(self, datum):                         # Insert at start ‡Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        link = Link(datum, self.getFirst())
        self.setFirst(link)

    def find(self, goal, key=identity):              # Return Link whose data-key == goal ‡Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        link = self.getFirst()
        while link is not None:
            if key(link.getData()) == goal:
                return link
            link = link.getNext()

    def search(self, goal, key=identity):            # Return datum for first match ‡Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        link = self.find(goal, key)
        return link.getData() if link is not None else None

    def insertAfter(self, goal, newDatum, key=identity):  # Insert after matching link ‡Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        link = self.find(goal, key)
        if link is None: return False
        newLink = Link(newDatum, link.getNext())
        link.setNext(newLink)
        return True

    # Deletion
    def deleteFirst(self):                           # Delete and return first datum ‡Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        if self.isEmpty():
            raise Exception("Cannot delete first of empty list")
        first = self.getFirst()
        self.setFirst(first.getNext())
        return first.getData()

    def delete(self, goal, key=identity):            # Delete first matching datum ‡Chapter 5 from Data Structures  Algorithms in Python_2022_ (Z-Library).pdf](file-service://file-QvZorXgAqV4DMd2C1kadPS)
        if self.isEmpty():
            raise Exception("Cannot delete from empty linked list")
        previous = self
        while previous.getNext() is not None:
            link = previous.getNext()
            if key(link.getData()) == goal:
                previous.setNext(link.getNext())
                return link.getData()
            previous = link
        raise Exception("No item with matching key found in list")


# ----------------------------------------------------------------------
# Recursive Knapsack Solver
# ----------------------------------------------------------------------

def knapsack(target, weights, index=0, current=None):
    """
    Recursively find all combinations of weights[index:] that sum to target.
    When target == 0, prints the current LinkedList of selected weights.
    """
    if current is None:
        current = LinkedList()

    # Base case: exact fit
    if target == 0:
        print(current)       # Each solution printed as a linked list
        return

    # No more items or target negative: dead end
    if index >= len(weights) or target < 0:
        return

    # 1) Include weights[index]
    #    Create a new list copying current and insert this weight
    incl = LinkedList()
    # Copy all items from current into incl
    def _copier(x, lst=incl): lst.insert(x)
    current.traverse(lambda x: incl.insert(x))
    incl.insert(weights[index])

    # Recurse with reduced target and next index
    knapsack(target - weights[index], weights, index + 1, incl)

    # 2) Exclude weights[index], move on
    knapsack(target, weights, index + 1, current)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------

if __name__ == "__main__":
    W = [11, 8, 7, 6, 5]
    T = 20
    print(f"Knapsack combinations for target = {T} and weights = {W}:")
    knapsack(T, W)