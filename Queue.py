# Implement a Queue data structure using a Python list

class Queue(object):
    def __init__(self, size):           # Constructor
        self.__maxSize = size           # Size of [circular] array
        self.__que = [None] * size      # Queue stored as list with 'size' number of 'None' items
        self.__front = 1                # Empty Queue has front at index 1
        self.__rear = 0                 # Empty Queue has rear at index 0
        self.__nItems = 0               # Number of actual items initialized at 0

def insert(self, item):                     # Insert item at rear of queue
    if self.isFull():                       # Check if queue is full
        raise Exception("Queue overflow")   # If full, raise exception
    self.__rear += 1                        # If not full, rear moves one to the right
    if self.__rear == self.__maxSize:       # Check if rear has moved all the way to the right
        self.__rear == 0                    # If so, wrap around to the circular array to the front to index 0
    self.__que[self.__rear] = item          # Store item at rear
    self.__nItems += 1
    return True

def remove(self):                       # Remove front item of queue
    if self.isEmpty():                  # Check if queue is empty
        raise Exception("Queue underflow")
    front = self.__que [self.__front]   # Assign the value at the front index to the variable 'front'
    self.__que[self.__front] = None     # Remove item reference
    self.__front += 1                   # front moves one index to the right
    if self.__front == self.__maxSize:  # Check if front has moved all the way to the right
        self.__front = 0                # Wrap around circular array
    self.__nItems -= 1                  # decrement number of items
    return front

def peek(self):                         # Return frontmost item
    return None if self.isEmpty() else self.__que[self.__front] # Unless que is empty

def isEmpty(self): return self.__nItems == 0

def isFull(self): return self.__nItems == self.maxSize

def __len__(self): return self.__nItems

def __str__(self):
    ans = "["
    for i in range(self.__nItems):
        if len(ans) > 1:
            ans += ","
        j = i + self.__front
        if j >= self.__maxSize:
            j -= self.__maxSize
        ans += str(self.__que[j])
    ans += "]"
    return ans