def identity(x): return x               # Identity function
from Array import *
from LinkStack import *

class Mergesort(object):                # An object to mergesort Arrays
    def __init__(self,                  # Constructor, takes the unordered
                 unordered,             # array and orders its items by using
                 key=identity):         # mergesort on their keys
        self.__arr = unordered          # Array starts unordered
        self.__key = key                # Key func. returns sort key of item
        n = len(unordered)              # Get number of items
        self.__work = Array(n)          # A work array of the same length
        for i in range(n):              # is needed to rearrange the items
            self.__work.insert(None)    # Work array is filled with None
        self.__todo = LinkStack()       # Stack to manage subproblems
        # seed stack with initial full-range sort task
        self.__todo.push([0, None, n])
        self.mergesort()                # Call mergesort on problem

    def mergesort(self):                # Perform mergesort on subrange
        while not self.__todo.isEmpty():    # Loop until no problems remain
            lo, mid, hi = self.__todo.peek()    # Get [lo, mid, hi] values
            print('Mergesort working on [lo, mid, hi] =',   # Show progress
                  self.__todo.peek(), 'at depth', len(self.__todo))
            if lo + 1 >= hi:            # If subrange has 1 or fewere items,
                self.__todo.pop()       # then done, and remove problem
                if self.__todo.isEmpty():   # If that was 1st problem
                    return              # then everything is done
                self.__todo.peek()[1] = lo  # Otherwise, store lo index in
                                            # caller's problem description for
                                            # 'mid' to signal completion
            elif mid is None:           # If mid is None, need to compute it
                mid = (lo + hi) // 2    # Find middle index, and add subtask
                self.__todo.push(       # for the lower half of subrange
                    [lo, None, mid])
            elif (mid == lo):           # If mid is lo, lower half is done
                self.__todo.push(       # add subtask for upper half of
                    [(lo + hi) // 2, None, hi]) # subrange
            else:                       # Both lower half and upper half done
                print('Merging ranges [', lo, ',', mid, ') with [',
                      mid, ',', hi, ')')
                self.merge(lo, mid, hi) # Merge the 2 sorted halves
                self.__todo.pop()       # Remove completed problem
                if self.__todo.isEmpty():   # If that was the 1st problem,
                    return              # then everything is done
                self.__todo.peek()[1] = lo  # Otherwise, signal caller
        raise Exception('Empty stack in mergesort')
