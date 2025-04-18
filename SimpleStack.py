# Implement a Stack data structure using a Python list

class Stack(object):
    def __init__(self, max):        # Constructor
        self.__stackList = [None] * max     # The stack stored as a list
        self.__top = -1             # No items initially

    def push(self, item):                       # Insert item at top of stack
        self.__top += 1                         # Advance the pointer
        self.__stackList[self.__top] = item     #Store item

    def pop(self):          # Remove top item from stack
        top = self.__stackList[self.__top]      # Top item
        self.__stackList[self.__top] = None     # Remove item reference
        self.__top -= 1                         # Decrease the pointer
        return top                              # Return top item

    def peek(self):                             # Return top item
        if not self.isEmpty():                  # If stack is not empty
            return self.__stackList[self.__top] # Return the top item

    def isEmpty(self):                          # Check if stack is empty
        return self.__top < 0                   # if the top item has index
                                                # less than 0, then return True

    def isFull(self):                           # Check if stack is full
        return self.__top >= len(self.__stackList)-1

    def __len__(self):                          # Return # of items on stack
        return self.__top + 1                   # Return index of top item plus 1

    def __str__(self):                          # Convert stack to string
        ans = "["                               # Start with left bracket
        for i in range(self.__top + 1):         # Loop through current items
            if len(ans) > 1:                    # Check if ans has more than one item ("[")
                ans+= ","                       # separate items with a comma
            ans += str(self.__stackList[i])     # Convert each item to a string, then
                                                # add it to the list ans
        ans += "]"                              # Close with right bracket
        return ans

    
        
                
        
