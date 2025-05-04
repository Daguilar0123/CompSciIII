# Implement a sortable Array data structure

class Array(object):
    def __init__(self, initialSize):    # Constructor
        self.__a = [None] * initialSize # The array storst as a list
        self.__nItems = 0               # No items in array initially

    def __len__(self):          # Special def for len() func
        return self.__nItems    # Return number of items

    def get(self, n):           # Return the value at index n
        if 0 <= n and n < self.__nItems:    # Check if n is in bounds, and
            return self.__a[n]              # only return item if in bounds

    def set(self, n, value):    # Set the value at index n
        if 0 <= n and n < self.__nItems:    # Check if n is in bounds, and
            self.__a[n] = value             # only set item if in bounds

    def swap(self, j, k):       # Swap the values at 2 indices
        if (0 <= j and j < self.__nItems and    # Check if indices are in
            0 <= k and k < self.__nItems):      # in bounds, before processing
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j] # Swap items

    def insert(self, item):     # Insert item at end
        self.__a[self.__nItems] = item          # Item goes at current end
        self.__nItems += 1                      # Increment number of items

    def find(self, item):       # Find index for item
        for j in range(self.__nItems):   # Iterate through all items
            if self.__a[j] == item:      # If found at index j,
                return j                 # then return index to element
        return -1                        # Item not found

    def search(self, item):              # Search for item
        return self.get(self.find(item)) # and return item if found

    def delete(self, item):              # Delete first occurrence
        for j in range(self.__nItems):   # of an item
            if self.__a[j] == item:      # If item found
                self.__nItems -= 1       # Decrement number of items
                for k in range(j, self__nItems): # Move items from
                    self.__a[k] = self.__a[k+1] # right over 1
                return True              # Return success flag
        return False                     # Item not found

    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__nItems):   # and apply a function
            function(self.__a[j])

    def __str__(self):                   # Special def for str() func
        ans = "["                        # Left bracket
        for i in range(self.__nItems):   # Loop through items
            if len(ans) > 1:             # Except next to left bracket,
                ans += ","               # separate items with comma
            ans += str(self.__a[i])      # Add string form of item
        ans += "]"                       # Close with right bracket
        return ans

    def bubbleSort(self):       # Sort comparing adjacent vals
        for last in range(self.__nItems-1, 0, -1): # Iterate from last item to
                                                   # first item, decrement by 1
            for inner in range(last):   # inner loop goes up to last
                if self.__a[inner] > self.__a[inner+1]:     # Check if left elem is greater
                                                            # than right elem
                    self.swap(inner, inner+1)   # Swap left and right

                    
                       
    def selectionSort(self):    # Sort by selecting min and
        for outer in range(self.__nItems-1):    # swapping min to leftmost
            min = outer         # Assume min is leftmost
            for inner in range(outer+1, self.__nItems):     # Hunt to right
                if self.__a[inner] < self.__a[min]:     # If we find new min,
                    min = inner         # update the min index

            # __a[min] is smallest among __a[outer]...__a[__nItems-1]
            self.swap(outer, min)       # Swap leftmost and min

    def insertionSort(self):        # Sort by repeated inserts
        for outer in range(1, self.__nItems):   # Mark one element
            temp = self.__a[outer]      # Store marked elem in temp
            inner = outer       # Inner loop starts at mark
            while inner > 0 and temp < self.__a[inner-1]:   # If marked
                self.__a[inner] = self.__a[inner-1]     # elem smaller, then
                inner -= 1      # shift elem to right
            self.__a[inner] = temp      # Move marked elem to 'hole'
            
            
        
            
