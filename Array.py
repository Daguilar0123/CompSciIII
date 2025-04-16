class Array(object):
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__a = [None] * capacity
        self.__nItems = 0

    def __len__(self):
        return self.__nItems

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def get(self, n):                   # Return the value at index n
        if 0<=n and n<self.__nItems:    # Check if n is in bounds
            return self.__a[n]          # Return if in bounds
        raise IndexError("Index out of bounds")
        
    def set(self, n, value):                # Set the value at index n
        if 0<=n and n<self.__nItems:        # Check if n is in bounds
            self.__a[n] = value             # only set value if in bounds
        else:
            raise IndexError("Index out of bounds")
    def insert(self, item):                 # Insert item at end
        if self.isFull():
            raise OverflowError("Array is full")
        else:
            self.__a[self.__nItems] = item
            self.__nItems += 1
    def find(self, item):                   # Find index for item
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
            return -1
    def search(self, item):                 # Search for item
        return self.get(self.find(item))    # and return item if found
    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k+1]
                return True
            return False
        
    def isFull(self):
        return self.__nItems == self.__capacity
     