import LinkedList

class Link(LinkedList.Link):            # One datum in a linked list
    def __init__(self, datum,           # Constructor with datum
                 next=None,             # and optional next and
                 previous=None):        # previous pointers
        self.__data = datum             # data
        self.__next = next              # Reference to next item in list
        self.__previous = previous      # Reference to previous item in list

    def getData(self): return self.__data   # Accessors
    def getNext(self):  return self.__next
    def getPrevious(self):  return self.__previous
    def setData(self, d): self.__data = d
    def setNext(self, link):            # Accessor that enforces type
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception("Next link must be Link or None")
    def setPrevious(self, link):        # Accessor that enforces type
        if link is None or isinstance(link, Link):
            self.__previous = link
        else:
            raise Exception("Previous link must be Link or None")
        
    def isFirst(self): return self.__previous is None

class DoublyLinkedList(LinkedList.LinkedList):
    def __init__(self):             # Constructor
        self.__first, self.__last = None, None

    def getFirst(self): return self.__first     # Accessors
    def getLast(self): return self.__last

    def setFirst(self, link):           # Set first link
        if link is None or isinstance(link, Link):  # Check type
            self.__first = link
            if (self.__last is None or  # If list was empty or
                link is None):          # list is being truncated
                self.__last = link      # update both ends
            else:
                raise Exception("First link must be Link or None")
            
    def setLast(self, link):            # Set last link
        if link is None or isinstance(link, Link):  # Check type
            self.__last = link
            if (self.__first is None or     # If list was empty or
                link is None):              # list is being truncated
                self.__first = link         # update both ends
        else:
            raise Exception("Last link must be Link or None")
        
    def traverseBackwards(          # Apply a function to all Links in list
            self, func=print):      # backwards from last to first
        link = self.getLast()       # Start with last link
        while link is not None:     # Keep going until no more links
            func(link)              # Apply the function to the link
            link = link.getPrevious()   # Move on to previous link

    def insertFirst(self, datum):       # Insert a new datum at start of list
        link = Link(datum,              # New link has datum
                    next=self.getFirst())   # and precedes current first
        if self.isEmpty():          # If list is empty,
            self.setLast(link)      # insert link as last (and first)
        else:                       # Otherwise, first Link in list
            self.getFirst().setPrevious(link)   # now has new Link before
            self.setFirst(link)     # Update first link

    insert = insertFirst            # Override parent class insert

    def insertLast(self, datum):    # Insert a new datum at end of list
        link = Link(datum,          # New link has datum
                    previous=self.getLast())    # and follows current last
        if self.isEmpty():          # If list is empty,
            self.setFirst(link)     # insert link as first (and last)
        else:                       # Otherwise, last Link in list
            self.getLast().setNext(link)    # now has new Link after
            self.setLast(link)      # Update last link

    def deleteFirst(self):          # Delete and return first link's data
        if self.isEmpty():          # If list is empty, raise exception
            raise Exception("Cannot delete first of empty list")
        first = self.getFirst()     # Store the first link
        self.setFirst(first.getNext())  # Remove first, advance to next
        if self.getFirst():         # If that leaves a link in the list,
            self.getFirst().setPrevious(None)   # Update its predecessor
        return first.getData()      # Return data from first link
    
    def deleteLast(self):           # Delete and return last link's data
        if self.isEmpty():          # If list is empty, raise exception
            raise Exception("Cannot delete last of empty list")
        last = self.getLast()       # Store the last link
        self.setLast(last.getPrevious())    # Remove last, advance to previous
        if self.getLast():          # If that leaves a link in the list,
            self.getLast().setNext(None)    # Update its successor
        return last.getData()       # Return data from last link