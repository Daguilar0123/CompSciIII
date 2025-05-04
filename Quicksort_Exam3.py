def identity(x):    return x    # Identity function
import SortArray

class Array(SortArray.Array):
    def partition(self, lo, hi, key=identity):
        pivot = self.get(hi)
        i = lo - 1
        for j in range(lo, hi):
            if key(self.get(j)) <= key(pivot):
                i += 1
                self.swap(i, j)
        # put pivot into position i + 1
        self.swap(i+1, hi)
        return i+1
    
if __name__=="__main__":
    # Test data from Problem #1
    values = [12, 5, 1, 7, 2, 9, 5, 3, 8, 4, 6]

    # Build and populate the Array
    arr = Array(len(values))
    for v in values:
        arr.insert(v)

    # Show before/after partition and pivot index
    print("Before partition:", arr)
    p = arr.partition(0, len(arr)-1)
    print("After partition: ", arr)
    print(f"Pivot {arr.get(p)} is now at index {p}")