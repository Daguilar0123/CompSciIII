"""
Problem 6.2:
Every positive integer can be divided into a set of integer factors.
The minimum set of factors must be a collection of prime numbers,
where a prime number is one that is only evenly divisible by 1 and itself.

Write a recursive function, factor(), that returns the list of integer
factors of x.


1. Only test factors between 2 and the square root of x (use lowest up to sqrt(x)).
2. Add an optional parameter to factor(x, lowest) for the lowest possible integer factor.
3. The recursive function should:
   a. Check base cases (0, 1, and negatives).
   b. If lowest evenly divides x (x % lowest == 0):
        - Add lowest to the factors of x divided by lowest.
   c. If lowest does NOT evenly divide x:
        - Look for factors with the next higher possible factor (lowest+1).
   d. A factor can appear more than once in the final list.
4. For negative x, return the factors of the positive version but with factor 1 replaced by -1.
5. Test on:
   -- Compound (nonprime) numbers
   -- Prime numbers
   -- Special cases of 0 and 1
   -- Negative integers

Use Chapter 5's LinkedList structure (plus __iter__ to traverse it).
"""

class Link:
    #One datum in a linked list.
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
    #Minimal Chapter 5 singly linked list.
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
        #Insert new datum at front of list (used to build factor lists).
        new_link = Link(datum, self.getFirst())
        self.setFirst(new_link)

    def __iter__(self):
        #Allow iteration: for d in linked_list.
        link = self.getFirst()
        while link is not None:
            yield link.getData()
            link = link.getNext()

    def __str__(self):
        pieces = [str(d) for d in self]
        return "[" + " > ".join(pieces) + "]"


def factor(x, lowest=2):
    """
    Recursive factor() per Problem 6.2:

    - Base cases:
        * x == 0  → special case of 0               # “special cases of 0 and 1”
        * x == 1  → special case of 1
        * x == -1 → handle negative 1

    - Negative integers:
        * Prepend -1 then factor(-x, lowest)
          # “factors of the positive version but with the factor 1 replaced by -1”

    - Prime detection:
        * If lowest*lowest > x, x is prime → insert(x)
          # “only the factors between 2 and the square root of x need to be tested”

    - Divide step:
        * If x % lowest == 0:
            -- Recursively factor(x//lowest, lowest)
            -- Then insert(lowest)
          # “If it does, then add lowest to the factors of x divided by lowest.”

    - Skip step:
        * Else → factor(x, lowest+1)
          # “If lowest doesn't evenly divide x, then look for factors with the next higher possible factor.”

    - A factor can appear > once in final list.
    """
    result = LinkedList()

    # ---- Base cases of 0, 1, and -1 ----
    if x == 0:
        result.insert(0)
        return result
    if x == 1:
        result.insert(1)
        return result
    if x == -1:
        result.insert(-1)
        return result

    # ---- Negative integer handling ----
    if x < 0:
        # factors of positive version but with factor 1 replaced by −1
        result.insert(-1)
        tail = factor(-x, lowest)
        for d in tail:          # traverse the positive factors
            result.insert(d)     # prepend so final order is correct
        return result

    # ---- Prime detection (lowest > sqrt(x)) ----
    if lowest * lowest > x:
        result.insert(x)  # x is prime, minimum set of primes includes x itself
        return result

    # ---- Divide step (x % lowest == 0) ----
    if x % lowest == 0:
        tail = factor(x // lowest, lowest)
        for d in tail:      # build up factors of (x//lowest)
            result.insert(d)
        result.insert(lowest)
        return result

    # ---- Skip to next higher integer factor ----
    return factor(x, lowest + 1)


# ---------------- Demo / Output ----------------
if __name__ == "__main__":
    # Test special cases of 0 and 1
    print("factor(0)  # special case 0 →", factor(0))
    print("factor(1)  # special case 1 →", factor(1))

    # Test prime numbers (minimum set of prime factors is itself)
    print("factor(2)  # prime number (evenly divisible only by 1 and itself) →", factor(2))
    print("factor(13) # prime number →", factor(13))

    # Test compound (nonprime) numbers
    print("factor(12) # factors of 12 → minimum set of primes →", factor(12))
    print("factor(60) # factors of 60 →", factor(60))

    # Test negative integer handling
    print("factor(-45) # negative integer → factors of 45 with -1 replacing 1 →", factor(-45))