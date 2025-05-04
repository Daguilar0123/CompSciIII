# MergesortViaStackClient.py

from Array import Array
from MergesortViaStack import Mergesort

def main():
    # The same 14 test values used in the textbook example
    values = [19, 49, 70, 72, 43, 80, 95, 
              46, 19, 18, 45, 6, 56, 85]

    # Build the Array
    array = Array(len(values))
    for v in values:
        array.insert(v)

    print("Initial array contains", len(array), "items:")
    array.traverse()
    print()

    # This will print the "Mergesort working on [lo, mid, hi] = …" lines
    Mergesort(array)

    print("\nAfter applying MergesortViaStack, array contains", 
          len(array), "items:")
    array.traverse()

if __name__ == "__main__":
    main()