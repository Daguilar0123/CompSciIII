class Link(object):             # One datum in a linked list
    def __init__(self, data, next=None):         # Constructor
        self.__data = data      # The datum for this link
        self.__next = next      # Reference to the next Link

    def getData(self):          # Return the datum stored in this link
        return self.__data
    
    def setData(self, datum):   # Change the datum in this Link
        self.__data = datum

    def getNext(self): return self.__next          # Return the next link

    def setNext(self, link):    # Change the next link to a new Link
        if link is None or isinstance(link, Link):      # Must be Link or None
            self.__next = link
        else:
            raise Exception("Next link must be Link or None")

    def isLast(self):               # Test if link is last in the chain
        return self.__next is None  # True if & only if no next Link
    
    def __str__(self):              # Test if link is last in the chain
        return str(self.getData())
    
def identity(x): return x           # Identity function
    
class LinkedList(object):       # A linked list of data elements
    def __init__(self):         # Constructor
        self.__first = None     # Reference to first Link

    def getFirst(self): return self.__first     # Return the first Link

    def setFirst(self, link):       # Change the first link to a new Link
        if link is None or isinstance(link, Link):      # It must be None or
            self.__first = link     # a Link object
        else:
            raise Exception("First link must be Link or None")
        
    def getNext(self): return self.getFirst()       # First link is next
    def setNext(self, link): self.setFirst(link)    # First link is next

    def isEmpty(self):              # Test for empty list 
        return self.getFirst() is None # True if & only if no 1st Link
    
    def first(self):                # Return the first item in the list
        if self.isEmpty():          # as l;ong as it is not empty
            raise Exception('No first item in empty list')
        return self.getFirst().getData()    # Return data item (not Link)
    
    def traverse(self,              # Apply a function to all items in list
                 func=print):       # with the default being to print
        link = self.getFirst()      # Start with first link
        while link is not None:     # Keep going until no more links
            func(link.getData())    # Apply the function to the item
            link = link.getNext()   # Move on to next link

    def __len__(self):              # Get length of list
        l = 0
        link = self.getFirst()      # Start with first link
        while link is not None:     # Keep going until no more links
            l += 1                  # Count Link in chain
            link = link.getNext()   # Move on to next l'ink
        return 1
    
    def __str__(self):              # Build a string representation
        result ="["                 # Enclose list in square brackets
        link = self.getFirst()      # Start with first link
        while link is not None:     # Keep going until no more links
            if len(result) > 1:     # After first link,
                result += " > "     # separate links with right arrowhead
            result += str(link)     # Append string version of link
            link = link.getNext()   # Move on to next link
        return result + "]"         # Close with square bracket