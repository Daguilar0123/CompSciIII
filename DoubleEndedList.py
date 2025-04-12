from LinkedList import *

class DoubleEndedList(LinkedList):          # A linked list with access to both
    def __init__(self):                     # ends of the list
        self.__first = None                 # Reference to first Link, if any
        self.__last = None                  # Reference to last link, if any

    def getFirst(self): return self.__first # Return the first link

    def setFirst(self, link):                       # Change the first link to a new Link
        if link is None or isinstance(link, Link):  # Must be Link or None
            self.__first = link                     # Update first link
            if (link is None or                     # When removing the first Link or
                self.getLast() is None):            # the last Link is not set,
                self.__last = link                  # then update the last link, too.
        else:
            raise Exception("First link must be Link or None")
        
        